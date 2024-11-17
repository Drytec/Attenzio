from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    est_full_name = models.CharField(max_length=100)
    est_id = models.IntegerField(unique=True, primary_key=True)
    est_phone = models.CharField(max_length=15, default="")
    est_tab = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    est_email = models.EmailField(max_length=100, unique=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.est_full_name