from django.db import models
from apps.user.models import CustomUser


class Teacher(CustomUser):
    teacher_document = models.IntegerField(unique=True)
    teacher_address = models.CharField(max_length=300, blank=True, null=True)
    teacher_picture = models.ImageField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "teacher"
        managed = False

    @property
    def is_validated(self):
        return self.validate

