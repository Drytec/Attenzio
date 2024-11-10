from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    document = models.IntegerField(unique=True)
    id = models.IntegerField(unique=True, primary_key=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="")
    validate = models.BooleanField(default=False, blank=True)
    picture = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    # Cambiar el campo de identificación principal
    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = ['name', 'lastName', 'email']

    def __str__(self):
        return f'{self.name} {self.lastName}'
#e