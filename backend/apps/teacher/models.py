from django.db import models
from apps.user.models import CustomUser


class Teacher(CustomUser):
    teacher_document = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100, db_column='teacher_full_name')
    email = models.EmailField(max_length=100, unique=True, db_column='teacher_email')
    teacher_address = models.CharField(max_length=300, blank=True, null=True)
    teacher_picture = models.ImageField(upload_to='teacher_pictures/', blank=True, null=True)
    password = models.CharField(max_length=30, null=False, db_column='teacher_pass')

    class Meta:
        db_table = "teacher"

    @property
    def is_validated(self):
        return self.validate
