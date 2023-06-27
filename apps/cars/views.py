from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import CarFilter
from .models import Car
from .serializers import CarSerializer


class CarListCreateApiView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filterset_class = CarFilter
    # def get_queryset(self):
    #     return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
