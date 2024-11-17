from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    # Aquí puedes agregar más campos personalizados según lo necesites
    picture = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.full_name