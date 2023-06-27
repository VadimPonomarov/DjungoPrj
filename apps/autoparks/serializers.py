from rest_framework import serializers

from apps.cars.serializers import CarSerializer

from .models import Autopark


class AutoparkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = Autopark
        fields = ('id', 'name', 'cars')
