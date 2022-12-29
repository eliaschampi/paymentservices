from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff == 1


class MyBaseModelPermision:
    def get_permissions(self):
        try:

            return [permission() for permission in self.permissionsByAction[self.action]]

        except KeyError:

            return [permission() for permission in self.permission_classes]


class CustomPermissionMixin:
    def handle_exception(self, exc):
        if isinstance(exc, PermissionDenied):
            return Response({
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": 'Ud no tiene permiso para acceder al recurso',
                "details": None,
                "success": False,
                "data": None,
            }, status=status.HTTP_403_FORBIDDEN)
        return super().handle_exception(exc)


class ServicePermisionMixin(CustomPermissionMixin, MyBaseModelPermision):
    permissionsByAction = {
        'list': [IsAuthenticated],
        'create': [IsAuthenticated, IsAdminUser],
        'post': [IsAuthenticated, IsAdminUser],
        'put': [IsAuthenticated, IsAdminUser],
        'destroy': [IsAuthenticated, IsAdminUser],
    }
