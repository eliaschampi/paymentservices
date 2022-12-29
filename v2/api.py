from rest_framework import viewsets
from .permissions import ServicePermisionMixin, PaymentUserPermisionMixin
from .response import ResponseMixin
from .models import Service, PaymentUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ServicesSerializer, PaymentUserSerializer
from .pagination import MyPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class ServiceApi(ServicePermisionMixin, ResponseMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    pagination_class = MyPagination
    serializer_class = ServicesSerializer
    authentication_classes = [JWTAuthentication]

class PaymentUserApi(PaymentUserPermisionMixin, ResponseMixin, viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all()
    pagination_class = MyPagination
    serializer_class = PaymentUserSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('payment_date', 'expiration_date')
    ordering = ('-created_at')
