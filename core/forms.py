from django.forms import ModelForm, forms
from django import  forms
from core.models import aula, teacher

class aulaForm(ModelForm):
    class Meta:
        model = aula
        fields = ['aula_id','nombre_aula','descripcion','fecha_inicio','fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}
class teacherForm(ModelForm):
    class Meta:
        model = teacher
        fields = ['documento','nombre','apellidos','direccion','telefono','email','password','foto']