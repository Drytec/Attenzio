from django.db import models
from ..customuser.models import CustomUser
from ..course.models import Course

# Create your models here.
class CustomUserCourse(models.Model):
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customusercourse'
        managed = False

    def __str__(self):
        return f'{self.custom_user_id}:{self.course_id}'

    def get_courses(self):
        if self.isTeacher():
            return Course.objects.filter(customusercourse__custom_user=self)
        elif self.isStudent():
            return Course.objects.filter(customusercourse__custom_user=self)
        return Course.objects.none()