from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import ServicePermisionMixin, PaymentUserPermisionMixin, UserPermisionMixin
from .response import ResponseMixin
from .models import Service, PaymentUser, ExpiredPayment
from authentication.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ServicesSerializer, PaymentUserSerializer, UserSerializer, ExpiredPaymentSerializer
from .pagination import MyPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .throttles import CustomRateThrottle, CustomPaymentRateThrottle


class ServiceApi(ServicePermisionMixin, ResponseMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    pagination_class = MyPagination
    serializer_class = ServicesSerializer
    authentication_classes = [JWTAuthentication]
    throttle_classes = [CustomRateThrottle]


class PaymentUserApi(PaymentUserPermisionMixin, ResponseMixin, viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all()
    pagination_class = MyPagination
    serializer_class = PaymentUserSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("payment_date", "expiration_date")
    ordering = ("-created_at")
    throttle_classes = [CustomPaymentRateThrottle]


class ExpiredApi(ResponseMixin, generics.ListCreateAPIView):
    queryset = ExpiredPayment.objects.all()
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = ExpiredPaymentSerializer
    throttle_scope = "expired_throttle"
    throttle_classes = [CustomRateThrottle]

class UserApi(UserPermisionMixin, ResponseMixin, viewsets.ViewSet):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    throttle_classes = [CustomRateThrottle]

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):

        instance = self.queryset.get(pk=pk)

        serializer = self.serializer_class(
            instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        password = request.data.get("password")
        if password is not None:
            instance.set_password(password)
            instance.save()
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)
