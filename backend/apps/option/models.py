from django.db import models
from ..question.models import Question

# Create your models here.
class Option(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField,
    option_id = models.IntegerField(primary_key=True),

    class Meta:
        db_table = "option"

    def __str__(self):
        return f'{self.option_id}'
