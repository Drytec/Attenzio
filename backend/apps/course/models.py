from django.db import models

from apps.user.models import CustomUser

# Create your models here.
class Course(models.Models):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=300)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        db_table = 'course'
        managed = False

    def __str__(self):
        return self.course_name