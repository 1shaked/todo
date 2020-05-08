from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['phone',] 
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email


class Todos(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.CASCADE)
    header = models.CharField(max_length=150)
    task = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    background = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.header


class Products(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    url = models.URLField(null=False, max_length=350)
    update_time = models.IntegerField()

    def __str__(self):
        return self.name
    