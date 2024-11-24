from django.db import models

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