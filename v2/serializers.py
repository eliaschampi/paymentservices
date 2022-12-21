from rest_framework import serializers
from .models import Service, PaymentUser, ExpiredPayment
from django.utils import timezone


class ServicesSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        required=True,
        max_length=40,
        error_messages={'required': 'Nombre es obligatorio'}
    )
    description = serializers.CharField(
        required=True,
        max_length=300,
        error_messages={'required': 'Descripción es obligatorio'}
    )

    logo = serializers.CharField(max_length=100)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'logo']


class PaymentUserSerializer(serializers.ModelSerializer):

    service_id = serializers.IntegerField(
        error_messages={'required': 'Servicio es obligatorio'}
    )

    class Meta:
        model = PaymentUser

        fields = ['id', 'user_id', 'service_id',
                  'amount', 'payment_date', 'expiration_date']

        required_fields = ['user_id', 'service_id',
                           'amount', 'payment_date', 'expiration_date']

    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a 0")
        if value > 10000:
            raise serializers.ValidationError(
                "El monto debe ser mayor a 10000")
        return value

    def validate_payment_date(self, value):

        if value <= timezone.now():
            raise serializers.ValidationError(
                "La fecha de expiración debe ser posterior a hoy")
        return value

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)


class ExpiredPayment(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = ('payment_user_id', 'penalty_fee_amount')

    def validate_penalty_fee_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "El monto debe ser mayor que cero."
            )
        return value
