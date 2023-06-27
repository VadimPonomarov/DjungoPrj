from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'year', 'seats', 'body_type', 'engine_volume', 'price')
