from django.db import models
from ..course.models import Course
from ..material.models import Material

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True)
    session_date_start = models.TimeField(blank=True)
    session_date_end = models.TimeField(blank=True)
    session_description = models.CharField(max_length=300, blank=True)
    qrCode = models.CharField(max_length=300, blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "session"
        managed = False

    def __str__(self):
        return f'{self.sesion_id}'

class Question(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    question_id = models.AutoField(primary_key=True),

    class Meta:
        db_table = "question"

    def __str__(self):
        return f'{self.question_id}'

class Option(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False),
    option_id = models.AutoField(primary_key=True),

    class Meta:
        db_table = "option"

    def __str__(self):
        return f'{self.option_id}'

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_link = models.CharField(max_length=300)

    class Meta:
        db_table = 'material'
        managed = False

    def __str__(self):
        return f'{self.material_id}'

class SessionMaterial(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='sessionMaterial')

    class Meta:
        db_table = 'sessionmaterial'
        managed = False

    def __str__(self):
        return f'{self.material_id}:{self.session_id}'