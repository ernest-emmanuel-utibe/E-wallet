from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

