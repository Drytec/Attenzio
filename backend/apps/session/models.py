from django.db import models
from ..course.models import Course

# Create your models here.

class Session(models.Model):
    """
    Modelo que representa una sesión dentro de un curso.

    Una sesión tiene atributos como el nombre, la fecha de inicio y fin, la descripción, y un código QR
    asociado. Además, está relacionada con un curso específico.

    Atributos:
        - session_id: Identificador único de la sesión (clave primaria).
        - session_name: Nombre de la sesión.
        - session_date_start: Hora de inicio de la sesión.
        - session_date_end: Hora de finalización de la sesión.
        - session_description: Descripción de la sesión.
        - qr_code: Código QR asociado a la sesión.
        - course_id: Relación con el modelo `Course`, indicando el curso al que pertenece la sesión.

    Metadatos:
        - db_table: Nombre de la tabla en la base de datos ("session").
        - managed: Indica que Django no gestionará la migración de esta tabla (establecido a `False`).

    Método especial:
        - __str__: Representación en forma de cadena del objeto (devuelve el `session_id`).
    """
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True)
    session_date_start = models.TimeField(blank=True)
    session_date_end = models.TimeField(blank=True)
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
    Modelo que representa una pregunta dentro de una sesión.

    Cada pregunta tiene un texto y está asociada a una sesión específica.

    Atributos:
        - question_id: Identificador único de la pregunta (clave primaria).
        - session_id: Relación con el modelo `Session`, indicando la sesión a la que pertenece la pregunta.
        - question_text: Texto de la pregunta.

    Metadatos:
        - db_table: Nombre de la tabla en la base de datos ("question").

    Método especial:
        - __str__: Representación en forma de cadena del objeto (devuelve el `question_id`).
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
    Modelo que representa una opción de respuesta para una pregunta.

    Cada opción tiene un texto y un indicador de si es la respuesta correcta. Está asociada a una pregunta.

    Atributos:
        - option_id: Identificador único de la opción (clave primaria).
        - question_id: Relación con el modelo `Question`, indicando la pregunta a la que pertenece la opción.
        - option_text: Texto de la opción de respuesta.
        - is_correct: Booleano que indica si la opción es la respuesta correcta.

    Metadatos:
        - db_table: Nombre de la tabla en la base de datos ("option").

    Método especial:
        - __str__: Representación en forma de cadena del objeto (devuelve el `option_id`).
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
    Modelo que representa un material relacionado con las sesiones.

    Cada material tiene un enlace que lo identifica y puede estar asociado a varias sesiones a través de
    la tabla intermedia `MaterialSession`.

    Atributos:
        - material_id: Identificador único del material (clave primaria).
        - material_link: Enlace al material.

    Metadatos:
        - db_table: Nombre de la tabla en la base de datos ("material").
        - managed: Indica que Django no gestionará la migración de esta tabla (establecido a `False`).

    Método especial:
        - __str__: Representación en forma de cadena del objeto (devuelve el `material_id`).
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
    Modelo que representa la relación entre un material y una sesión.

    Este modelo permite asociar un material con una o más sesiones a través de una clave foránea
    hacia `Material` y `Session`.

    Atributos:
        - material_session_id: Identificador único de la relación (clave primaria).
        - material_id: Relación con el modelo `Material`, indicando el material asociado.
        - session_id: Relación con el modelo `Session`, indicando la sesión asociada.

    Metadatos:
        - db_table: Nombre de la tabla en la base de datos ("materialsession").
        - managed: Indica que Django no gestionará la migración de esta tabla (establecido a `False`).

    Método especial:
        - __str__: Representación en forma de cadena del objeto (devuelve la relación entre `material_id` y `session_id`).
    """
    material_session_id = models.AutoField(primary_key=True, db_column='material_session_id', unique=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, db_column='material_id')
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE, db_column='session_id')

    class Meta:
        db_table = 'materialsession'
        managed = False

    def __str__(self):
        return f'{self.material_id}:{self.session_id}'
