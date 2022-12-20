from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: HttpResponse("Hola mundo")),
    path("users/", include("user.urls"))
]
