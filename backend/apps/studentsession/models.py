from django.db import models

# Create your models here.
class StudentSession(models.Model):

    est_id = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='est_id')
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, db_column='session_id')
    class Meta:
        db_table = "StudentSession"

