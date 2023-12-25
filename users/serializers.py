from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False)


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(source="auth_token.key")

    class Meta:
        model = User
        fields = [
            "token",
        ]
