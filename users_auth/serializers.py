from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import CustomUser, Todos
from django.conf import settings


class UserCreateSerializerImplement(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = settings.AUTH_USER_MODEL
        fields = '__all__'


class UserDisplay(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = settings.AUTH_USER_MODEL
        fields = '__all__'




class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = '__all__'
