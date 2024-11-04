from django.forms import ModelForm, forms
from django import  forms
from core.models import aula, Teacher
from django.contrib.auth import get_user_model
from django import forms
from core.models import Teacher

User = get_user_model()
class aulaForm(ModelForm):
    class Meta:
        model = aula
        fields = ['aula_id','nombre_aula','descripcion','fecha_inicio','fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}


class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['documento', 'nombre', 'apellidos', 'email', 'direccion', 'telefono', 'foto', 'password']