from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#using AbstractUser creating your custom User model.
class User(AbstractUser):
    phone_number = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    