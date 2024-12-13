from django.db import models
from ..customuser.models import CustomUser

# Create your models here.

class Course(models.Model):
    """
    Modelo que representa un curso.

    Atributos:
        - course_id: ID único del curso (clave primaria).
        - course_name: Nombre del curso.
        - course_schedule: Horario del curso.

    Meta:
        - db_table: Especifica el nombre de la tabla en la base de datos como 'course'.
        - managed: Indica que Django no gestionará la creación de esta tabla (para usar tablas preexistentes).

    Métodos:
        - __str__: Devuelve una representación en cadena del curso (su nombre).
    """
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=300)
    course_schedule = models.CharField(max_length=300)

    class Meta:
        db_table = 'course'
        managed = False

    def __str__(self):
        return self.course_name


class CustomUserCourse(models.Model):
    """
    Modelo que representa la relación entre un usuario y un curso.

    Atributos:
        - custom_user_course_id: ID único de la relación entre usuario y curso (clave primaria).
        - custom_user_id: Relación con el usuario (clave foránea hacia el modelo CustomUser).
        - course_id: Relación con el curso (clave foránea hacia el modelo Course).

    Meta:
        - db_table: Especifica el nombre de la tabla en la base de datos como 'customusercourse'.
        - managed: Indica que Django no gestionará la creación de esta tabla (para usar tablas preexistentes).

    Métodos:
        - __str__: Devuelve una representación en cadena de la relación usuario-curso (combinando los IDs del usuario y del curso).
    """
    custom_user_course_id = models.AutoField(primary_key=True, db_column='custom_user_course_id', unique=True)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='custom_user_id')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

    class Meta:
        db_table = 'customusercourse'
        managed = False

    def __str__(self):
        return f'{self.custom_user_id}:{self.course_id}'
