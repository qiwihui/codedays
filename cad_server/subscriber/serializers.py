from django.utils import timezone
from rest_framework import serializers
from subscriber.models import Subscriber


class SubscriberSerializer(serializers.Serializer):
    
    email = serializers.EmailField(error_messages={
        "blank": "请输入正确的邮箱",
        "invalid": "请输入正确的邮箱"
    })

    def validate_email(self, email):
        try:
            subscriber = Subscriber.objects.get(email=email)
        except Subscriber.DoesNotExist as e:
            return email
        if subscriber.status == 1:
            raise serializers.ValidationError("您已经订阅了我们的邮件。")
        else:
            # 重新发送邮件订阅
            return email

    def create(self, validated_data):
        email = validated_data.get("email")
        new_subscriber, created = Subscriber.objects.get_or_create(email=email)
        return new_subscriber
