from django.db import models
from apps.user.models import CustomUser

# Create your models here.
class Student(CustomUser):
    est_phone = models.CharField(max_length=10, blank=True, null=True)
    est_tab = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = "student"
