from django import forms

from .models import Student

class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Student
        fields = ['fullName', 'email', 'phone', 'tab', 'password']
        labels = {
            'fullName': 'Nombre Completo',
            'email': 'Email',
            'phone': 'Teléfono',
            'tab': 'Foto',
        }
