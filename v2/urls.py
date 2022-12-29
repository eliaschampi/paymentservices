from django.urls import path
from . import api

urlpatterns = [
    path(r'services/', api.ServiceList.as_view(), name='service-list'),
    path(r'services/create', api.ServiceCreate.as_view(), name='service-create'),
    path(r'services/update/<int:pk>', api.ServiceUpdate.as_view(), name='service-update'),
    path(r'services/destroy/<int:pk>', api.ServiceDestroy.as_view(), name='service-destroy'),
]