import rest_framework.pagination
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import car_filtered_queryset
from .models import Car
from .serializers import Car_serializer


class CarListCreateApiView(ListCreateAPIView):
    serializer_class = Car_serializer
    queryset = Car.objects.all()
    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = Car_serializer
    queryset = Car.objects.all()
