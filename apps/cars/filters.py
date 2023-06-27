from django_filters import rest_framework as filters
from .models import Car


class CarFilter(filters.FilterSet):
    order = filters.OrderingFilter(fields=('id', 'model'))

    class Meta:
        model = Car
        fields = ('id', 'model')
