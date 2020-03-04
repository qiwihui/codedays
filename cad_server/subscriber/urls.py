from django.urls import path
from subscriber import views

urlpatterns = [
    path('subscribe', views.SubscriberView.as_view(), name='subscribe'),
    path('subscribe/confirm', views.SubscriptionConfirmation.as_view(), name='subscription_confirmation'),
    path('unsubscribe', views.UnsubscriberView.as_view(), name='unsubscribe'),
    # 获取已经接收过的问题
    path('subscribe/problems', views.SubscriberProblems.as_view(), name='subscribe_problems'),
    path('subscribe/problems/<int:pk>', views.SubscriberProblem.as_view(), name='subscribe_problem_one'),

    # login
    path('login', views.Login.as_view(), name='subscribe_problems'),

    # TODO: 支付
    # 检查支付状态
]
