from django.http import Http404
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from apps.autoparks.models import Autopark
from apps.autoparks.serializers import AutoparkSerializer
from apps.cars.serializers import CarSerializer


class AutoparkListCreateView(ListCreateAPIView):
    serializer_class = AutoparkSerializer
    queryset = Autopark.objects.prefetch_related('cars')


class AutoparkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoparkSerializer
    queryset = Autopark.objects.prefetch_related('cars')


class AutoparkCarCreateView(GenericAPIView):
    queryset = Autopark.objects.prefetch_related('cars')

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = CarSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        exists = Autopark.objects.filter(pk=pk).exists()

        if not exists:
            raise Http404()

        serializer.save(autopark_id=pk)
        return Response(serializer.data, status.HTTP_201_CREATED)
