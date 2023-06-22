from rest_framework import serializers
from .models import Car


class Car_serializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'year', 'seats', 'body_type', 'engine_volume', 'price')
