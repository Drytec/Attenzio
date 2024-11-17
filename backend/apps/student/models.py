from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Teacher(AbstractUser):
    fullName = models.CharField(max_length=100)
    id = models.IntegerField(unique=True, primary_key=True)
    phone = models.CharField(max_length=15, default="")
    tab = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    # Cambiar el campo de identificación principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.fullName