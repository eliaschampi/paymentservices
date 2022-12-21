from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import Service
from .serializers import ServicesSerializer
from .pagination import MyPagination

class ServiceListOrCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated, TokenAuthentication,)
    pagination_class = MyPagination

class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, TokenAuthentication,)
    lookup_field = "id"
