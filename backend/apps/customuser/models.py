from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from ..rol.models import Rol

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    custom_user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, null=True)
    media = models.ImageField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=30, blank=True)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')
    validated = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()
    class Meta:
        db_table = 'customuser'
        managed = False

    def __str__(self):
        return self.full_name

    def isTeacher(self):
        return self.rol_id == 1

    def isStudent(self):
        return self.rol_id == 2
    #Funcion solicitada por django para el manejo de superusuarios
    def get_by_natural_key(self, email):
        return self.objects.get(email=email)