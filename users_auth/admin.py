from django.contrib import admin
from .models import CustomUser, Products, Todos
# Register your models here.
admin.site.register(Products)
admin.site.register(CustomUser)
admin.site.register(Todos)