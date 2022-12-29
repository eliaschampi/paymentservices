from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.SimpleRouter()
router.register(r"services", api.ServiceApi, basename="services")
router.register(r"payments", api.PaymentUserApi, basename="payments")
router.register(r"users", api.UserApi, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path(r"expireds/", api.ExpiredApi.as_view(), name="expireds")
]
