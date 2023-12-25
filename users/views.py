
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponseBadRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.serializers import LoginSerializer, LoginResponseSerializer

__all__ = [
    "LoginView"
]


class LoginView(views.APIView):
    @swagger_auto_schema(
        operation_summary="Авторизация",
        request_body=LoginSerializer(),
        responses={status.HTTP_200_OK: LoginResponseSerializer()},
    )
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        username = validated_data.get("username")
        password = validated_data.get("password")

        user = authenticate(request=request, username=username, password=password)
        if not user:
            return HttpResponseBadRequest()

        Token.objects.get_or_create(user=user)
        login(request, user)

        return Response(LoginResponseSerializer(user).data)

