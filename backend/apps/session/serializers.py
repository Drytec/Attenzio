from rest_framework import serializers
from .models import Session, Material, Question, Option

class SessionSerializer(serializers.ModelSerializer):
    """
    Serializer para representar una sesión educativa. Este serializer se utiliza para serializar
    los datos de la sesión, incluyendo su identificación, nombre, descripción y las fechas de inicio y fin.

    Campos:
        - session_id (int): El identificador único de la sesión.
        - session_name (str): El nombre de la sesión.
        - session_description (str): Una descripción de la sesión.
        - session_date_start (datetime): La fecha y hora de inicio de la sesión.
        - session_date_end (datetime): La fecha y hora de finalización de la sesión.
    """

    class Meta:
        model = Session
        fields = ['session_id', 'session_name', 'session_description', 'session_date_start', 'session_date_end']

class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer para representar los materiales asociados a una sesión. Este serializer se utiliza
    para serializar los materiales, incluyendo un enlace al archivo/material.

    Campos:
        - material_id (int): El identificador único del material.
        - material_link (str): El enlace al material o archivo.
    """

    class Meta:
        model = Material
        fields = ['material_id', 'material_link']

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer para representar las preguntas asociadas a una sesión. Este serializer serializa
    las preguntas, junto con el texto de la pregunta y el ID de la sesión a la que pertenece.

    Campos:
        - question_id (int): El identificador único de la pregunta.
        - question_text (str): El texto de la pregunta.
        - session_id (int): El identificador de la sesión a la que la pregunta pertenece.
    """

    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'session_id']

class OptionSerializer(serializers.ModelSerializer):
    """
    Serializer para representar las opciones asociadas a una pregunta. Este serializer serializa
    las opciones de respuesta para una pregunta, incluyendo el texto de la opción y si es la correcta.

    Campos:
        - option_id (int): El identificador único de la opción.
        - option_text (str): El texto de la opción.
        - is_correct (bool): Indica si la opción es correcta o no.
        - question_id (int): El identificador de la pregunta a la que pertenece la opción.
    """

    class Meta:
        model = Option
        fields = ['option_id', 'option_text', 'is_correct', 'question_id']
