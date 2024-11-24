from django.forms import ModelForm
from .models import Course
from django import forms
from django.contrib.auth.models import User

class courseForm(ModelForm):
    class Meta:
        model = Course
        #aqui definimos lo s atributos que seran solicitados en el formulario
        fields = ['course_name','course_id']

        #aqui definimos como se veran las etiquetas en el formulario
        labels = {
            'course_name': 'Nombre de la Sesión',
            'course_id': 'ID del curso',

        }

