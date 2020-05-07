from django.urls import path, include, re_path
from .views import ProductsList, ProductView, TodosList, TodoView
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('jwt/', include('djoser.urls')),
    path('jwt/', include('djoser.urls.jwt')), # (r'^auth/', include('djoser.urls.jwt'))
    path('products-list/<int:pk>/', ProductsList.as_view(), name='products-list'),
    path('product-view/<int:pk>/', ProductView.as_view(), name='products-view'),
    path('todos/', TodosList.as_view(), name='todos'),
    re_path(r'^todo-view/(?P<pk>\d+)/', TodoView.as_view(), name='todo-view'),
]
