from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_schedule']
        labels = {
            'course_name': 'Nombre del curso',
            'course_schedule': 'Descripcion del Horario del Curso',
        }
