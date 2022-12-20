from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from .pagination import StandardResultsSetPagination


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.get_queryset().order_by("id")
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ["user_id", "service", "payment_date"]

    throttle_scope = 'payments_v1'
