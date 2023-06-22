from django.urls import path

from apps.autoparks.views import AutoparkListCreateView, AutoparkRetrieveUpdateDestroyView, AutoparkCarCreateView

urlpatterns = [
    path('', AutoparkListCreateView.as_view()),
    path('/<int:pk>', AutoparkRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/car', AutoparkCarCreateView.as_view())
]