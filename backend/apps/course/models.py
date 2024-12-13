from django.db import models
from ..customuser.models import CustomUser

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=300)
    course_schedule = models.CharField(max_length=300)

    class Meta:
        db_table = 'course'
        managed = False

    def __str__(self):
        return self.course_name

class CustomUserCourse(models.Model):
    custom_user_course_id = models.AutoField(primary_key=True, db_column='custom_user_course_id', unique=True)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='custom_user_id')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

    class Meta:
        db_table = 'customusercourse'
        managed = False

    def __str__(self):
        return f'{self.custom_user_id}:{self.course_id}'