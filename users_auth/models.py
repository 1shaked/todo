from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['username', 'phone'] 
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email


class Todos(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='user',
        on_delete=models.CASCADE)
    header = models.CharField(max_length=150)
    task = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    background = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.header
