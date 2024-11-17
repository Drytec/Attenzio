from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    tab = models.ImageField(upload_to='photos/', max_length=100, blank=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.fullName