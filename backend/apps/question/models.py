from django.db import models
from backend.apps.teacher.models import Teacher

# Create your models here.
class Session(models.Model):
    sessionId = models.IntegerField(primary_key=True)
    sessionMaterial = models.TextField(max_length=100)
    qrCode = models.ImageField(max_length=100)
    dateSession = models.DateField(null=True)
    hourSession = models.TimeField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='sessions')

    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "session"

    def __str__(self):
        return f'{self.sesion_id}'
