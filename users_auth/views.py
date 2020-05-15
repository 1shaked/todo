from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import TodosSerializer
from .models import Todos

# Create your views here.
# todos View

class TodosList(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class  = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        print(self.request.query_params)
        print(self.request.query_params)
        return Todos.objects.filter(user = user_id)


class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class  = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]