from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    documento = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, default="")
    validar = models.BooleanField(default=False, blank=True)
    foto = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    # Cambiar el campo de identificación principal
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
#e