from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#definimos los atributos de las entidades
class teacher(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=100,default='Nombre')
    apellidos = models.CharField(max_length=100,default='Apellidos')
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(default=000000000)
    #esta funcion registra la hora en la que se crea pero esta dando error
    #created= models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.nombre

    #definimos los atributos de las entidades
class aula(models.Model):
    aula_id = models.IntegerField(default=0)
    nombre_aula = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    #created= models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    #archivos_aula = models.FileField(max_length=100, null=True, blank=True)
    #hay que cambiar la llave foranea de user a teacher
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_aula + ' -por: ' + self.user.username
