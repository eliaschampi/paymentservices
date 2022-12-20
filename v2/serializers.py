from rest_framework import serializers
from .models import Service


class ServicesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=40)
    description = serializers.CharField(max_length=300)
    logo = serializers.CharField(max_length=100)

    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'logo')
