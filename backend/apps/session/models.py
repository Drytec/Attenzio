from django.db import models
from apps.teacher.models import Teacher

# Create your models here.
class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_name = models.TextField(max_length=100)
    session_material = models.TextField(max_length=100)
    session_description = models.TextField(max_length=100)
    qrCode = models.ImageField(max_length=100,blank=True)
    session_date_start = models.DateField(null=True)
    session_date_end = models.DateField(null=True)
    session_hour = models.TimeField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='session')

    class Meta:
        db_table = "session"

    def __str__(self):
        return f'{self.sesion_id}'
