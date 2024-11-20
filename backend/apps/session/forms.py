from django.forms import ModelForm
from .models import Session
from django import forms
from django.contrib.auth.models import User

class sessionForm(ModelForm):
    class Meta:
        model = Session
        #aqui definimos lo s atributos que seran solicitados en el formulario
        fields = ['session_name', 'session_description', 'session_date_start', 'session_date_end']

        #aqui definimos como se veran las etiquetas en el formulario
        labels = {
            'session_name': 'Nombre de la Sesión',
            'session_description': 'Descripción',
            'session_date_start': 'Fecha de Inicio',
            'session_date_end': 'Fecha de Fin',
        }

        # Widgets para campos de fecha y hora
        widgets = {
            'session_date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'session_date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
