from django.db import models
from kb.models import Problem


class Subscriber(models.Model):
    """订阅者
    """
    STATUS_SUBSCRIBED = 1
    STATUS_UNSUBSCRIBED = 0
    # 邮箱
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    # 状态 0-未验证 1-已经验证
    status = models.PositiveIntegerField(default=0)
    # 创建时间
    created_time = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    # 更新时间
    updated_time = models.DateTimeField(null=False, blank=True, auto_now=True)
    # 是否购买了解答
    is_vip = models.BooleanField(default=False)
    # TODO: 服务信息，时间

    class Meta:
        app_label = "subscriber"
        db_table = "subscriber"

    def __str__(self):
        return self.email


class SentProblems(models.Model):
    # 任务ID
    task_id = models.UUIDField(null=True)
    # 是否发送
    sent = models.BooleanField(default=False)
    # 订阅者
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    # 问题
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    # 发送时间
    date = models.DateField(auto_now_add=True)
    # 解答
    solutions = models.CharField(max_length=128, null=True)

    class Meta:
        app_label = "subscriber"
        db_table = "sent_problem"

    def __str__(self):
        return f'sub: {self.subscriber}, pro: {self.problem}'
