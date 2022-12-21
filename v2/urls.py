from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ServiceListOrCreate, ServiceRetrieveUpdateDestroyAPIView

#router = DefaultRouter()

urlpatterns = [
    path("services/", ServiceListOrCreate.as_view(), name="service"),
    path("services/", ServiceRetrieveUpdateDestroyAPIView.as_view(), name="service")
]
