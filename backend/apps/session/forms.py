from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.forms import ModelForm
from .models import Question, Option, Material
from django import forms
from .models import Session

class SessionForm(forms.ModelForm):
    """
    Formulario para la creación o edición de una sesión.

    Campos:
    - session_name: Nombre de la sesión.
    - session_description: Descripción de la sesión.
    - session_date_start: Fecha de inicio de la sesión.
    - session_date_end: Fecha de finalización de la sesión.

    Etiquetas:
    - session_name: 'Nombre de la Sesión'
    - session_description: 'Descripción'
    - session_date_start: 'Fecha de Inicio'
    - session_date_end: 'Fecha de Fin'
    """
    class Meta:
        model = Session
        fields = ['session_name', 'session_description', 'session_date_start', 'session_date_end']
        labels = {
            'session_name': 'Nombre de la Sesión',
            'session_description': 'Descripción',
            'session_date_start': 'Fecha de Inicio',
            'session_date_end': 'Fecha de Fin',
        }

class QuestionForm(ModelForm):
    """
    Formulario para la creación de una pregunta en una sesión.

    Campos:
    - question_text: Enunciado de la pregunta.

    Etiqueta:
    - question_text: 'Enunciado de la Pregunta'
    """
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Enunciado de la Pregunta',
        }

class OptionForm(ModelForm):
    """
    Formulario para la creación de una opción para una pregunta.

    Campos:
    - option_text: Texto de la opción.
    - is_correct: Indica si la opción es correcta.

    Etiquetas:
    - option_text: 'Texto de la Opción'
    - is_correct: '¿Es Correcta?'

    Widgets personalizados:
    - option_text: Agrega clases CSS y un texto de marcador de posición.
    - is_correct: Aplica una clase para checkbox.
    """
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
    """
    Formulario para la creación de un material asociado a una sesión.

    Campos:
    - material_link: Enlace al material (URL).

    Etiqueta:
    - material_link: 'Link al material'
    """
    class Meta:
        model = Material
        fields = ['material_link']
        labels = {
            'material_link': 'Link al material'
        }

    def clean_material_link(self):
        """
        Valida el enlace del material para asegurar que sea una URL válida.

        Si el enlace no es válido, se lanza una excepción de validación.
        """
        material_link = self.cleaned_data.get('material_link')
        validate_url = URLValidator()
        try:
            validate_url(material_link)
        except ValidationError:
            raise ValidationError("El enlace proporcionado no es válido.")
        return material_link
