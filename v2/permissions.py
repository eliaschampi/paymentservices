from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff == 1


class CustomPermissionMixin:
    def handle_exception(self, exc):
        if isinstance(exc, PermissionDenied):
            return Response({
                'message': 'Ud no tiene permiso para acceder al recurso',
                'success': False,
                'code': status.HTTP_403_FORBIDDEN,
            }, status=status.HTTP_403_FORBIDDEN)
        return super().handle_exception(exc)
