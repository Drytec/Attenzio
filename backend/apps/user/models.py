from multiprocessing.util import MAXFD

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    #document = models.CharField(max_length=20)
    #address = models.CharField(max_length=100)
    #picture = models.ImageField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Incrementado a 128 caracteres
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    class Meta:
        db_table = "customuser"
        managed = True

    def __str__(self):
        return self.full_name