from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    profFullName = models.CharField(max_length=100)
    profCedula = models.IntegerField(unique=True)
    profId = models.IntegerField(unique=True, primary_key=True)
    profAddress = models.CharField(max_length=100)
    validate = models.BooleanField(default=False, blank=True)
    profPicture = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    profEmail = models.EmailField(max_length=100, unique=True)

    # Cambiar el campo de identificación principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'document']

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.fullName

    @property
    def is_validated(self):
        return self.validate
