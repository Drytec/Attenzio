from django import forms

from .models import Teacher

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Teacher
        fields = ['document', 'name', 'lastName', 'email', 'address', 'phone', 'picture', 'password']
        labels = {
            'document': 'Documento',
            'name': 'Nombre',
            'lastName': 'Apellidos',
            'email': 'Email',
            'address': 'Dirección',
            'phone': 'Teléfono',
            'picture': 'Foto',
        }
