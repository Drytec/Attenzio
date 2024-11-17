from django.db import models
from backend.apps.user.models import CustomUser

# Create your models here.
class Student(CustomUser):
    full_name = models.CharField(max_length=100, db_column='est_full_name')
    email = models.EmailField(max_length=100, unique=True, db_column='est_email')
    est_phone = models.CharField(max_length=10, blank=True, null=True)
    est_tab = models.BinaryField(blank=True, null=True)
    password = models.CharField(max_length=30, null=False, db_column='est_pass')

    class Meta:
        db_table = "student"
