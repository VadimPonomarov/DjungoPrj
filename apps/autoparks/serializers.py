from rest_framework import serializers
from apps.cars.serializers import Car_serializer
from .models import Autopark


class Autopark_serializer(serializers.ModelSerializer):
    cars = Car_serializer(read_only=True, many=True)

    class Meta:
        model = Autopark
        fields = ('id', 'name', 'cars')
