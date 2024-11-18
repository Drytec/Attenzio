from django import forms

from .models import Teacher

class TeacherRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Teacher
        fields = ['teacher_document', 'full_name', 'email', 'teacher_address', 'teacher_picture', 'password']
        labels = {
            'teacher_document': 'Documento',
            'full_name': 'Nombre Completo',
            'email': 'Email',
            'teacher_address': 'Dirección',
            'teacher_picture': 'Foto',
        }
