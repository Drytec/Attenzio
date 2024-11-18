from django.db import models
from backend.apps.session.models import Session

# Create your models here.
class Question(models.Model):
    questionId = models.IntegerField(primary_key=True)
    questionText = models.TextField(max_length=200)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='sessions')

    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "question"

    def __str__(self):
        return f'{self.questionId}'
