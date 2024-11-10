from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['documento', 'nombre', 'apellidos', 'email', 'direccion', 'telefono', 'foto', 'password']

