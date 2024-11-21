from django.db import models

# Create your models here.
class Rol(models.Model):
    rol_id = models.IntegerField(primary_key=True)
    rol_name = models.CharField(max_length=100)
    class Meta:
        db_table = "rol"
        managed = False
    def __str__(self):
        return f'{self.rol_id}'


