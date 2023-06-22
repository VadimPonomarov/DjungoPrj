from django.urls import path

from apps.cars.views import CarListCreateApiView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateApiView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]
