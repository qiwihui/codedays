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
            Subscriber.objects.get(email=email)
        except Subscriber.DoesNotExist as e:
            return email
        raise serializers.ValidationError("用户已经订阅")

    def create(self, validated_data):
        new_subscriber = Subscriber()
        new_subscriber.email = validated_data.get("email")
        new_subscriber.satus = Subscriber.STATUS_UNSUBSCRIBED
        new_subscriber.created_time = timezone.now()
        new_subscriber.updated_time = timezone.now()
        new_subscriber.save()
        return new_subscriber
