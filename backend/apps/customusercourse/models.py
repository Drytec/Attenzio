from django.db import models
from ..customuser.models import CustomUser
from ..course.models import Course

from django.db import models
from ..customuser.models import CustomUser
from ..course.models import Course

class CustomUserCourse(models.Model):
    custom_user_course_id = models.AutoField(primary_key=True, db_column='custom_user_course_id', unique=True)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='custom_user_id')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

    # Definir la clave primaria compuesta
    class Meta:
        db_table = 'customusercourse'
        managed = False

    def __str__(self):
        return f'{self.custom_user_id}:{self.course_id}'
