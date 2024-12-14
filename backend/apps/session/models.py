from django.db import models
from ..course.models import Course
from ..customuser.models import CustomUser


# Create your models here.

class Session(models.Model):
    """
    Representa una sesión en un curso, que puede incluir preguntas, materiales y un código QR.

    Atributos:
    - session_id: Identificador único de la sesión (clave primaria).
    - session_name: Nombre de la sesión.
    - session_date_start: Fecha de inicio de la sesión.
    - session_date_end: Fecha de finalización de la sesión.
    - session_description: Descripción de la sesión.
    - qr_code: Código QR asociado con la sesión.
    - course_id: Relación con el modelo `Course`, indicando el curso al que pertenece la sesión.
    """
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True)
    session_date_start = models.CharField(blank=True)
    session_date_end = models.CharField(blank=True)
    session_description = models.CharField(max_length=300, blank=True)
    qr_code = models.CharField(max_length=300, blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

    class Meta:
        db_table = "session"
        managed = False

    def __str__(self):
        return f'{self.sesion_id}'

class Question(models.Model):
    """
    Representa una pregunta dentro de una sesión.

    Atributos:
    - session_id: Relación con el modelo `Session`, indicando la sesión a la que pertenece la pregunta.
    - question_text: Texto de la pregunta.
    - question_id: Identificador único de la pregunta (clave primaria).
    """
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, db_column='session_id', related_name='questions')
    question_text = models.CharField(max_length=200)
    question_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = "question"

    def __str__(self):
        return f'{self.question_id}'

class Option(models.Model):
    """
    Representa una opción para una pregunta específica en una sesión.

    Atributos:
    - question_id: Relación con el modelo `Question`, indicando la pregunta a la que pertenece la opción.
    - option_text: Texto de la opción.
    - is_correct: Booleano que indica si la opción es la correcta.
    - option_id: Identificador único de la opción (clave primaria).
    """
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='question_id', related_name='question')
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    option_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = "option"

    def __str__(self):
        return f'{self.option_id}'

class Material(models.Model):
    """
    Representa un material relacionado con una sesión.

    Atributos:
    - material_id: Identificador único del material (clave primaria).
    - material_link: Enlace al material (por ejemplo, un archivo o recurso externo).
    """
    material_id = models.AutoField(primary_key=True)
    material_link = models.CharField(max_length=300)

    class Meta:
        db_table = 'material'
        managed = False

    def __str__(self):
        return f'{self.material_id}'

class MaterialSession(models.Model):
    """
    Relaciona materiales con sesiones específicas.

    Atributos:
    - material_session_id: Identificador único de la relación entre material y sesión.
    - material_id: Relación con el modelo `Material`, indicando el material asociado.
    - session_id: Relación con el modelo `Session`, indicando la sesión asociada.
    """
    material_session_id = models.AutoField(primary_key=True, db_column='material_session_id', unique=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, db_column='material_id')
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, db_column='session_id')

    class Meta:
        db_table = 'materialsession'
        managed = False

    def __str__(self):
        return f'{self.material_id}:{self.session_id}'

class CustomUserOption(models.Model):
    """
    Relaciona a los usuarios con las opciones que han seleccionado en una pregunta.

    Atributos:
    - custom_user_option_id: Identificador único de la relación entre el usuario y la opción seleccionada.
    - custom_user_id: Relación con el modelo `CustomUser`, indicando el usuario que seleccionó la opción.
    - option_id: Relación con el modelo `Option`, indicando la opción seleccionada por el usuario.
    """
    custom_user_option_id = models.AutoField(primary_key=True, db_column='custom_user_option_id', unique=True)
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='custom_user_id')
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE, db_column='option_id')

    class Meta:
        db_table = 'customuseroption'
        managed = False

    def __str__(self):
        return f'{self.custom_user_id}:{self.option_id}'
