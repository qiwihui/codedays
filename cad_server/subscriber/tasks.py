# Create your tasks here
from __future__ import absolute_import, unicode_literals
import uuid
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.utils import timezone
from subscriber import utils, models as sub_models
from kb import models as kb_models
from kb import serializers as kb_serializers

logger = get_task_logger(__name__)


@task(name='task_send_subscription_email')
def task_send_subscription_email(email, subscription_confirmation_url):
    return utils.send_subscription_email(email, subscription_confirmation_url)


@task(name='task_send_problem_email')
def task_send_problem_email(email, problem, previous_solutions=None):
    ok = utils.send_problem_email(email, problem, previous_solutions)
    sub_models.SentProblems.objects.filter(subscriber__email=email).update(sent=ok)


@periodic_task(
    run_every=(crontab(minute=0, hour=6)),
    # run_every=(crontab(minute='*')),
    name="task_send_daily_problem"
)
def task_send_daily_problem():
    """
    Send daily problem
    """
    all_subscribers = sub_models.Subscriber.objects.filter(status=1)
    for subscriber in all_subscribers:
        task_id = str(uuid.uuid4())
        logger.info(f"send_daily_problem @ {subscriber.email}")
        # get problem
        current_sending_problem, created = sub_models.SentProblems.objects.get_or_create(
            subscriber=subscriber,
            defaults={
                "problem": kb_models.Problem.objects.get(order=1)
            }
        )

        # 订阅确认之后当天不发送
        if current_sending_problem.date == subscriber.updated_time.date():
            continue
        
        # 今天已经发送
        if current_sending_problem.sent and current_sending_problem.date == timezone.now().date():
            logger.info("今天已经发送了")
            continue
        
        # 昨天已经发送，问题加1
        if current_sending_problem.sent and current_sending_problem.date < timezone.now().date():
            logger.info("今天新发送")
            # TODO: 判断是否还有新问题
            try:
                current_sending_problem.problem = kb_models.Problem.objects.get(order=current_sending_problem.problem.order+1)
            except kb_models.Problem.DoesNotExist as e:
                # 没有新问题了，需要添加新问题
                logger.error("没有新问题了，需要添加新问题")
                continue

        # 未发送
        if not current_sending_problem.sent:
            # 今天未发送
            pass

        previous_solutions = None
        
        if current_sending_problem.problem.order > 1:
            previous_problem = kb_models.Problem.objects.get(order=current_sending_problem.problem.order-1)
            if subscriber.is_vip:
                solutions = previous_problem.solutions.all()
            else:
                solutions = previous_problem.solutions.filter(level=0)
            solutions = kb_serializers.SolutionSerializer(solutions, many=True)
            previous_solutions = solutions.data[:]
        
        # TODO: 记录日志
        problem = kb_serializers.ProblemSerializer(current_sending_problem.problem).data
        sent = task_send_problem_email.delay(
            subscriber.email,
            problem,
            previous_solutions=previous_solutions
        )
        
        sub_models.SentProblems.objects.update_or_create(
            subscriber=subscriber,
            defaults={
                "task_id": task_id,
                "problem": current_sending_problem.problem,
                "date": timezone.now().date,
            },
        )
