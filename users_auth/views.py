from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import ProductsSerializer, TodosSerializer
from .models import Products, Todos

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


#prouduct vies
class ProductsList(APIView):
    """
    View to list all products in the system.

    * Requires token authentication.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,pk ,format=None):
        """
        Return a list of all users.
        """
        # user = request.data['user']
        products = Products.objects.filter(user=pk)
        # products = Products.objects.filter(user=user)

        products_serializer = ProductsSerializer(products, many=True) 
        # print(products_serializer.data)
        return Response(products_serializer.data)

class ProductsList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,pk ,format=None):
        """
        Return a list of all users.
        """
        # user = request.data['user']
        products = Products.objects.filter(user=pk)
        # products = Products.objects.filter(user=user)

        products_serializer = ProductsSerializer(products, many=True) 
        # print(products_serializer.data)
        return Response(products_serializer.data)


class ProductView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class  = ProductsSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        print(self.request.query_params)
        return Products.objects.filter(user = user_id)





    




# class ProductView(APIView):
    """
    View to list all products in the system.

    * Requires token authentication.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self, request,pk ,format=None):
    #     """
    #     Return a a product by id
    #     """
    #     products = Products.objects.filter(id=pk)

    #     products_serializer = ProductsSerializer(products, many=True) 
    #     # print(products_serializer.data)
    #     return Response(products_serializer.data)

    # def post(self, request, pk):
    #     print(request.data)
    #     return Response(request.data)