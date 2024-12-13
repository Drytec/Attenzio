from django.forms import ModelForm
from .models import Course
from django import forms

class CourseForm(ModelForm):
    """
    Formulario para la creación y edición de un curso.

    Este formulario utiliza el modelo `Course` y permite a los usuarios
    proporcionar el nombre del curso y su horario.

    Atributos:
    - `course_name`: El nombre del curso.
    - `course_schedule`: La descripción del horario del curso.

    La clase `Meta` especifica que este formulario está basado en el modelo `Course`
    y define los campos que estarán disponibles en el formulario, así como las etiquetas
    para cada campo.

    Métodos:
    - `__init__`: Este método es automáticamente generado por Django para inicializar los campos del formulario.
    """
    class Meta:
        model = Course  # El modelo con el que se relaciona este formulario
        fields = ['course_name', 'course_schedule']  # Los campos del formulario
        labels = {  # Etiquetas personalizadas para los campos del formulario
            'course_name': 'Nombre del curso',
            'course_schedule': 'Descripción del horario del curso',
        }

class CourseIdInputForm(forms.Form):
    """
    Formulario para ingresar el ID de un curso.

    Este formulario permite al usuario ingresar el identificador numérico de un curso.
    El campo `course_id` valida que el valor proporcionado sea un número entero mayor que 0.

    Atributos:
    - `course_id`: Un campo de tipo entero que permite ingresar el ID de un curso.

    Métodos:
    - `__init__`: Este método es automáticamente generado por Django para inicializar el formulario.
    """
    course_id = forms.IntegerField(
        label='ID del Curso',  # Etiqueta que se muestra junto al campo
        min_value=1,  # Valida que el valor sea mayor o igual a 1
        widget=forms.NumberInput(attrs={  # Configura el widget para el campo
            'placeholder': 'Ingresa el ID del curso',  # Placeholder en el campo de entrada
            'class': 'form-control'  # Clase CSS para el campo
        }),
    )


