from django import forms

from .models import Student

class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = Student
        fields = ['full_name', 'email', 'est_phone', 'est_tab', 'password']
        labels = {
            'full_name': 'Nombre Completo',
            'email': 'Email',
            'est_phone': 'Teléfono',
            'est_tab': 'Foto',
        }
