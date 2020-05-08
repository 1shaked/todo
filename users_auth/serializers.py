from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import CustomUser, Products, Todos


class UserCreateSerializerImplement(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password', 'phone')


class UserDisplay(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = '__all__'




class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'