from django.db import models


# Create your models here.
class sesion(models.Model):
    sesion_id = models.IntegerField(primary_key=True)
    sesion_name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sesion_name} - por:'
