from django.urls import path
from rest_framework import routers
from . import api

router = routers.SimpleRouter()
router.register(r'services', api.ServiceApi)

urlpatterns = router.urls
