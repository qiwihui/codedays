import logging
import time
from django.urls import reverse
from django.utils import timezone
from django.forms import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from subscriber.serializers import SubscriberSerializer
from subscriber.models import Subscriber, SentProblems
from subscriber import utils
from kb import models as kb_models
from kb.serializers import ProblemSerializer

logger = logging.getLogger("warning")


class SubscriberView(APIView):

    permission_class = (AllowAny, )

    def post(self, request):
        """新建订阅
        """
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            new_sub = serializer.save()
            # TODO 发送邮件任任务
            token = utils.encrypt(utils.SEPARATOR.join([new_sub.email, str(time.time())]))
            entrypoint = request.build_absolute_uri(reverse('subscription_confirmation'))
            subscription_confirmation_url = entrypoint.replace('api/v1/', '') + "?token=" + token
            ok = utils.send_subscription_email(new_sub.email, subscription_confirmation_url)
            
            if ok:
                msg = "邮件已经发送，请点击确认链接完成订阅。同时查看垃圾邮件中"
                # messages.success(request, msg)
                data = {
                    "error": False,
                    "message": msg
                }
            else:
                data = {
                    "error": True,
                    "message": "订阅错误，请重新订阅"
                }
            
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "message": "订阅错误"
            }
            print(serializer.errors)
        return Response(data, status=status.HTTP_200_OK)


class SubscriptionConfirmation(APIView):

    permission_class = (AllowAny, )

    def post(self, request):
        """确认订阅
        """
        token = request.data.get("token", None)
        data = {
            "error": False,
            "message": ""
        }

        if not token:
            logger.warning("Invalid Link ")
            data["error"] = True
            data["message"] = "确认邮件不正确"
            return Response(data, status=status.HTTP_200_OK)

        token = utils.decrypt(token)
        if token:
            token = token.split(utils.SEPARATOR)
            # time when email was sent , in epoch format. can be used for later calculations
            initiate_time = token[1]
            if float(initiate_time) + 24.0*60*60 < time.time():
                data = {
                    "error": True,
                    "message": "确认邮件已过时，请重新确认"
                }
                return Response(data, status=status.HTTP_200_OK)
            email = token[0]
            print(email)
            try:
                subscribe_model_instance = Subscriber.objects.get(email=email)
                subscribe_model_instance.status = Subscriber.STATUS_SUBSCRIBED
                # subscribe_model_instance.updated_time = timezone.now()
                subscribe_model_instance.save()
            except Subscriber.DoesNotExist as e:
                logger.warning(e)
                data = {
                    "error": True,
                    "message": "确认邮件错误，请重新确认"
                }
                return Response(data, status=status.HTTP_200_OK)
        else:
            logger.warning("Invalid token ")
            data = {
                "error": True,
                "message": "确认邮件错误，请重新确认"
            }

        return Response(data, status=status.HTTP_200_OK)


class UnsubscriberView(APIView):

    permission_class = (AllowAny, )

    def post(self, request):
        """取消订阅
        
        Args:
            request ([type]): [description]
        """
        # https://dailycodingproblem.com/unsubscribe?unsubscribeKey=06190567d339790553dca0ddbe18d6cd3a306054707b647d9083e501dbb6cf1537399aed
        pass


class SubscriberProblems(APIView):

    def get(self, request):
        """获取用户收到的问题
        """
        try:
            sent_problem = SentProblems.objects.get(subscriber__email=request.user.email)
            order = sent_problem.problem.order if sent_problem.sent else sent_problem.problem.order-1
        except SentProblems.DoesNotExist as e:
            sent_problem = None
            order = 0

        problems = kb_models.Problem.objects.filter(order__lte=order).values()
        return Response(data={"data": {"problems": problems}})


class SubscriberProblem(APIView):

    def get(self, request, pk):
        """获取单个问题的信息
        
        Args:
            pk ([type]): [description]
        """
        try:
            sent_problem = SentProblems.objects.get(subscriber__email=request.user.email)
            order = sent_problem.problem.order if sent_problem.sent else sent_problem.problem.order-1
        except SentProblems.DoesNotExist as e:
            sent_problem = None
            order = 0
        try:
            target_problem = kb_models.Problem.objects.get(id=pk, order__lte=order)
        except kb_models.Problem.DoesNotExist as e:
            target_problem = None
        if target_problem is not None:
            problem = ProblemSerializer(target_problem).data
            problem["solutions"] = target_problem.solutions.all().values()
        else:
            problem = {}
        
        return Response(data={"data": {"problems": problem}})
    

class Login(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {"data": {}}
            return Response(data=data)
        else:
            data = {"data": {}}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        