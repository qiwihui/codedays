from django.urls import path
from subscriber import views

urlpatterns = [
    path(r'subscribe', views.SubscriberView.as_view(), name='subscribe'),
    path(r'subscribe/confirm', views.SubscriptionConfirmation.as_view(), name='subscription_confirmation'),
    path(r'unsubscribe/', views.UnsubscriberView.as_view(), name='unsubscribe'),
]
