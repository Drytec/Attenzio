from django.forms import ModelForm
from .models import sesion
from django import forms
from django.contrib.auth.models import User

class sessionForm(ModelForm):
    class Meta:
        model = sesion
        #aqui definimos lo s atributos que seran solicitados en el formulario
        fields = ['session_name', 'description', 'date_start', 'date_end']

        #aqui definimos como se veran las etiquetas en el formulario
        labels = {
            'session_name': 'Nombre de la Sesión',
            'description': 'Descripción',
            'date_start': 'Fecha de Inicio',
            'date_end': 'Fecha de Fin',
        }

        # Widgets para campos de fecha y hora
        widgets = {
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
