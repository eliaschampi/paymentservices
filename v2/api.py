from rest_framework import viewsets
from .permissions import ServicePermisionMixin
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
