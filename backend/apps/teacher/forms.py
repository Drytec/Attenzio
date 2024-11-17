from django import forms

from .models import Teacher

class TeacherRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Teacher
        fields = ['document', 'fullName', 'email', 'address', 'phone', 'picture', 'password']
        labels = {
            'document': 'Documento',
            'fullName': 'Nombre Completo',
            'email': 'Email',
            'address': 'Dirección',
            'phone': 'Teléfono',
            'picture': 'Foto',
        }
