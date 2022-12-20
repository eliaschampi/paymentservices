from .api import PaymentViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"payments", PaymentViewSet, "payments")

urlpatterns = router.urls