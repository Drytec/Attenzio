from django.forms import ModelForm
from core.models import aula, teacher

class aulaForm(ModelForm):
    class Meta:
        model = aula
        fields = ['nombre_aula','descripcion','fecha_inicio','fecha_fin']

class teacherForm(ModelForm):
    class Meta:
        model = teacher
        fields = ['documento','nombre','apellidos','direccion','telefono','email','password','foto']