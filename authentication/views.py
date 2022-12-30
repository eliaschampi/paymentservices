from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from .models import User


class SingUpView(generics.GenericAPIView):

    serializer_class = SignUpSerializer

    def post(self, request: Request):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            data={
                "status_code": status.HTTP_201_CREATED,
                "message": "Usuario creado correctamente",
                "data": serializer.data,
                "success": True
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):

    def post(self, request: Request):

        email: str = request.data.get("email")
        password: str = request.data.get("password")

        user: User = authenticate(email=email, password=password)

        if user is None:
            return Response(
                data={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "credenciales de autenticación no validos",
                    "data": None,
                    "tokens": None,
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        user = User.objects.get(email=email)

        return Response(
            data={
                "status_code": status.HTTP_200_OK,
                "message": "Inicio de sesión exitoso",
                "data": GetUserSerializer(user).data,
                "tokens": create_jwt_pair_for_user(user=user),
                "success": True
            },
            status=status.HTTP_200_OK
        )

    def get(self, request: Request):

        return Response(
            data={"user": str(request.user), "auth": str(request.auth)},
            status=status.HTTP_200_OK
        )
