from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    documento = models.IntegerField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0)
    validar = models.BooleanField(default=False, null=True, blank=True)
    foto = models.ImageField(max_length=100, blank=True)
    email = models.EmailField(max_length=100,unique=True)
    # esta es la verificacion para el administrador, aun no se implementa por facilidad para pruebas
    #no se añade al formulario
    #verificado = models.BooleanField(default=False, null=True, blank=True)

    # Cambiar el campo de identificación principal
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'


# Modelo aula con ForeignKey a Teacher
class aula(models.Model):
    aula_id = models.IntegerField(default=0)
    nombre_aula = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_aula} - por: {self.user.nombre}'
