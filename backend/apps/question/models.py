from django.db import models
from backend.apps.session.models import Session

# Create your models here.
class Question(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session')
    question_text = models.CharField(max_length=200)
    question_id = models.IntegerField(primary_key=True),

    class Meta:
        db_table = "question"

    def __str__(self):
        return f'{self.question_id}'
