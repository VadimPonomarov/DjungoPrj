from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from .models import User

UserModel: User = get_user_model()


class UserFilter(filters.FilterSet):
    email_startswith = filters.CharFilter('email', 'istartswith')
    name_startswith = filters.CharFilter('name', 'name__istartswith')
    surname_startswith = filters.CharFilter('surname', 'surname__istartswith')

    email_contains = filters.CharFilter('email', 'icontains')
    name_contains = filters.CharFilter('name', 'name__icontains')
    surname_contains = filters.CharFilter('surname', 'surname__icontains')

    order = filters.OrderingFilter(fields=(
        'id',
        'email',
        ('profile__name', 'name'),
        ('profile__surname', 'surname'),
        ('profile__age', 'age'),
    ))
