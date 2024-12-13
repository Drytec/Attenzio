from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.forms import ModelForm, modelformset_factory
from .models import Session, Question, Option, Material
from django import forms

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['session_name', 'session_description', 'session_date_start', 'session_date_end']
        labels = {
            'session_name': 'Nombre de la Sesión',
            'session_description': 'Descripción',
            'session_date_start': 'Fecha de Inicio',
            'session_date_end': 'Fecha de Fin',
        }
        widgets = {
            'session_date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'session_date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Enunciado de la Pregunta',
        }

class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct']
        labels = {
            'option_text': 'Texto de la Opción',
            'is_correct': '¿Es Correcta?',
        }
        widgets = {
            'option_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el texto de la opción'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['material_link']
        labels = {
            'material_link': 'Link al material'
        }

    def clean_material_link(self):
        material_link = self.cleaned_data.get('material_link')
        validate_url = URLValidator()
        try:
            validate_url(material_link)  # Intenta validar el enlace
        except ValidationError:
            raise forms.ValidationError("El enlace proporcionado no es una URL válida.")
        return material_link