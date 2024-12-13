from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class Rol(models.Model):
    rol_id = models.IntegerField(primary_key=True)
    rol_name = models.CharField(max_length=100)
    class Meta:
        db_table = "rol"
        managed = False
    def __str__(self):
        return f'{self.rol_id}'
class CustomUser(AbstractBaseUser, PermissionsMixin):
    custom_user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, null=True)
    media = models.CharField(max_length=300, blank=True)
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

    @property
    def isTeacher(self):
        return self.rol_id_id == 1

    @property
    def isStudent(self):
        return self.rol_id_id == 2

    @property
    def isAdmin(self):
        return self.rol_id_id == 3

    def get_by_natural_key(self, email):
        return self.objects.get(email=email)