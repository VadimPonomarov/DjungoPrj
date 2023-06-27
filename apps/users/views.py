from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model

from .models import User
from .filters import UserFilter

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filterset_class = UserFilter
