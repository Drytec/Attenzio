from django import forms
from .models import CustomUser, Rol

class TeacherRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'email', 'address', 'picture', 'password']
        labels = {
            'document': 'Documento',
            'full_name': 'Nombre Completo',
            'email': 'Email',
            'address': 'Dirección',
            'picture': 'Foto',
        }

    def save(self, commit=True):
    # Crea la instancia de CustomUser sin guardarla todavía
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encripta la contraseña

    # Obtiene o crea el rol 'teacher' en la tabla Rol
        teacher_role = Rol.objects.get(rol_name='teacher')  # Obtiene el rol
        user.rol_id = teacher_role  # Asigna el rol al usuario

        if commit:
            user.save()
        return user




class userStudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'email', 'address', 'picture', 'password']
        labels = {
            'document': 'Documento',
            'full_name': 'Nombre Completo',
            'email': 'Email',
            'address': 'Dirección',
            'picture': 'Foto',
    }
    def save(self, commit=True):
        # Crea la instancia de CustomUser sin guardarla todavía
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encripta la contraseña

        # Obtiene o crea el rol 'teacher' en la tabla Roll
        student_role, created = Roll.objects.get_or_create(rol_name='student')

        # Asigna el rol al nuevo usuario
        user.rol_id = student_role

        if commit:
            user.save()
        return user