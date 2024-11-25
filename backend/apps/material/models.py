from django.db import models

# Create your models here.
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_link = models.CharField(max_length=300)

    class Meta:
        db_table = 'material'
        managed = False

    def __str__(self):
        return f'{self.material_id}'
