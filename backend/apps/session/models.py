from django.db import models
from apps.teacher.models import Teacher

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True, null=True)
    session_date_start = models.TimeField(blank=True, null=True)
    session_date_end = models.TimeField(blank=True, null=True)
    session_description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = "session"
        managed = False

    def __str__(self):
        return f'{self.sesion_id}'
