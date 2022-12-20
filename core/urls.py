from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: HttpResponse("Hola mundo")),
    path("users/", include("authentication.urls")),
    re_path(r"^api/v1/", include("v1.urls"))
]
