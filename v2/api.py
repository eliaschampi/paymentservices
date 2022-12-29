from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser, CustomPermissionMixin
from rest_framework.response import Response
from .models import Service, PaymentUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ServicesSerializer, PaymentUserSerializer
from .pagination import MyPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    pagination_class = MyPagination
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Correctamente listado'
        context['success'] = True
        context['code'] = status.HTTP_200_OK
        return context


class ServiceCreate(CustomPermissionMixin, generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Correctamente creado',
            'success': True,
            'code': status.HTTP_201_CREATED,
            'results': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class ServiceUpdate(CustomPermissionMixin, generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = [JWTAuthentication]

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Correctamente modificado',
            'success': True,
            'code': status.HTTP_200_OK,
            'results': serializer.data
        }, status=status.HTTP_201_CREATED)


class ServiceDestroy(CustomPermissionMixin, generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, pk=None):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response({
            'message': 'Correctamente eliminado',
            'success': True,
            'code': status.HTTP_200_OK,
            'results': []
        }, status=status.HTTP_201_CREATED)


class PaymentUserList(generics.ListAPIView):
    queryset = PaymentUser.objects.all()
    pagination_class = MyPagination
    serializer_class = PaymentUserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('payment_date', 'expiration_date')
    ordering = ('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Correctamente listado'
        context['success'] = True
        context['code'] = status.HTTP_200_OK
        return context


class PaymentUserCreate(CustomPermissionMixin, generics.CreateAPIView):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Correctamente creado',
            'success': True,
            'code': status.HTTP_201_CREATED,
            'results': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class PaymentUserUpdate(CustomPermissionMixin, generics.UpdateAPIView):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = [JWTAuthentication]

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Correctamente modificado',
            'success': True,
            'code': status.HTTP_200_OK,
            'results': serializer.data
        }, status=status.HTTP_201_CREATED)


class PaymentUserDestroy(CustomPermissionMixin, generics.DestroyAPIView):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, pk=None):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response({
            'message': 'Correctamente eliminado',
            'success': True,
            'code': status.HTTP_200_OK,
            'results': []
        }, status=status.HTTP_201_CREATED)
