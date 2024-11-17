from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    fullName = models.CharField(max_length=100)
    document = models.IntegerField(unique=True)
    id = models.IntegerField(unique=True, primary_key=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="")
    validate = models.BooleanField(default=False, blank=True)
    picture = models.ImageField(upload_to='photos/', max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

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
