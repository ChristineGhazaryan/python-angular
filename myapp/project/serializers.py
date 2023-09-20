from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('status', 'user_ptr')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'id')
