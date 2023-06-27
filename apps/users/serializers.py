from django.db import transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import User, UserProfile

UserModel: User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'surname', 'age',)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile',)
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile',
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        profile = UserProfile.objects.create(**profile)
        user = UserModel.objects.create_user(**validated_data, profile=profile)
        return user
