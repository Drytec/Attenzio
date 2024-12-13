from django.db import models
from ..customuser.models import CustomUser

# Create your models here.

class Course(models.Model):
    """
    Modelo que representa un curso.

    Atributos:
    - `course_id`: Identificador único para el curso (clave primaria).
    - `course_name`: Nombre del curso.
    - `course_schedule`: Horario o programación del curso.

    La tabla de la base de datos correspondiente a este modelo es `course`, y no está siendo gestionada automáticamente por Django (por lo que el atributo `managed` es `False`).

    Métodos:
    - `__str__`: Devuelve el nombre del curso cuando el objeto es convertido a cadena.
    """
    course_id = models.AutoField(primary_key=True)  # Identificador único del curso (clave primaria)
    course_name = models.CharField(max_length=300)  # Nombre del curso
    course_schedule = models.CharField(max_length=300)  # Horario o programación del curso

    class Meta:
        db_table = 'course'  # Nombre de la tabla en la base de datos
        managed = False  # Django no gestionará esta tabla (no la creará ni migrará)

    def __str__(self):
        return self.course_name  # Devuelve el nombre del curso al convertir el objeto a cadena


class CustomUserCourse(models.Model):
    """
    Modelo que representa la relación entre un usuario y un curso.

    Atributos:
    - `custom_user_course_id`: Identificador único para la relación (clave primaria).
    - `custom_user_id`: Relación con el usuario que está inscrito en el curso.
    - `course_id`: Relación con el curso al que el usuario está inscrito.

    La tabla de la base de datos correspondiente a este modelo es `customusercourse`, y no está siendo gestionada automáticamente por Django (por lo que el atributo `managed` es `False`).

    Métodos:
    - `__str__`: Devuelve una cadena que representa la relación entre el usuario y el curso, en el formato `usuario:curso`.
    """
    custom_user_course_id = models.AutoField(primary_key=True, db_column='custom_user_course_id', unique=True)  # Identificador único de la relación
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='custom_user_id')  # Relación con el usuario
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')  # Relación con el curso

    class Meta:
        db_table = 'customusercourse'  # Nombre de la tabla en la base de datos
        managed = False  # Django no gestionará esta tabla (no la creará ni migrará)

    def __str__(self):
        return f'{self.custom_user_id}:{self.course_id}'  # Devuelve una cadena representando la relación usuario-curso
