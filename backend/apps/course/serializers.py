from rest_framework import serializers
from .models import Course, CustomUserCourse

from rest_framework import serializers
from .models import Course, CustomUserCourse

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Course. Este serializer convierte un objeto de tipo `Course`
    en formato JSON y viceversa.

    Este serializer incluye los campos esenciales para representar los cursos, como el
    identificador, el nombre y el horario del curso.

    Campos:
        - course_id (int): El identificador único del curso.
        - course_name (str): El nombre del curso.
        - course_schedule (str): El horario en el que se imparte el curso.
    """

    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_schedule']

class CustomUserCourseSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Course. Este serializer convierte un objeto de tipo `CustomUserCourse`
    en formato JSON y viceversa.

    Este serializer incluye una relación anidada con el serializer `CourseSerializer`
    para representar los datos de los cursos relacionados con los usuarios.

    Campos:
        - custom_user_course_id (int): El identificador único de la relación entre un usuario y un curso.
        - custom_user_id (int): El identificador del usuario asociado a este curso.
        - course (CourseSerializer): Información detallada del curso, serializada a través del `CourseSerializer`.
    """


    course = CourseSerializer()

    class Meta:
        model = CustomUserCourse
        fields = ['custom_user_course_id', 'custom_user_id', 'course']
