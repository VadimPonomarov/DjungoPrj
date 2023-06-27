from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators as V
from django.db import models
from core.enums.regex_enum import RegExEnum

from core.models import BaseModel
from .managers import UserManager


class UserProfile(BaseModel):
    class Meta:
        db_table = 'user_profile'
        ordering = ('name', 'surname')

    name = models.CharField(max_length=50,
                            validators=[V.RegexValidator(regex=RegExEnum.NAME.pattern, message=RegExEnum.NAME.msg)])
    surname = models.CharField(max_length=50, validators=[V.RegexValidator(regex=RegExEnum.SURNAME.pattern,
                                                                           message=RegExEnum.SURNAME.msg)])
    age = models.IntegerField(validators=[V.MinValueValidator(16),
                                          V.MinValueValidator(150)])


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ('id', 'email')

    email = models.EmailField(unique=True, validators=[
        V.RegexValidator(regex=RegExEnum.USER_EMAIL.pattern, message=RegExEnum.USER_EMAIL.msg)])
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(regex=RegExEnum.PASSWORD.pattern, message=RegExEnum.PASSWORD.msg)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='user')

    USERNAME_FIELD = 'email'

    objects = UserManager()
