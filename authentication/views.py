from django.contrib.auth import authenticate
from rest_framework import viewsets, generics, status
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
                "message": "Usuario creado correctamente",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):

    def post(self, request: Request):

        email: str = request.data.get("email")
        password: str = request.data.get("password")

        user: User = authenticate(email=email, password=password)

        if user is None:
            return Response(data={"message": "Sus credenciales son incorrectas"})

        id_user = User.objects.get(email=email)

        return Response(
            data={
                "message": "Inicio de sesión exitoso",
                "id": id_user.id,
                "tokens": create_jwt_pair_for_user(user=user)
            },
            status=status.HTTP_200_OK
        )

    def get(self, request: Request):

        return Response(
            data={"user": str(request.user), "auth": str(request.auth)},
            status=status.HTTP_200_OK
        )



class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
