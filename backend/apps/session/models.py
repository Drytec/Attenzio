from django.db import models
from ..course.models import Course
from ..material.models import Material

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True)
    session_date_start = models.TimeField(blank=True)
    session_date_end = models.TimeField(blank=True)
    session_description = models.CharField(max_length=300, blank=True)
    qrCode = models.CharField(max_length=300, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "session"
        managed = False

    def __str__(self):
        return f'{self.sesion_id}'
