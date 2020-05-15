from django.contrib import admin
from .models import CustomUser, Todos
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Todos)