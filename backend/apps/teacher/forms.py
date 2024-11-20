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

    def save(self, commit=True):
        # Crea y guarda el nuevo Teacher, incluyendo la contraseña
        teacher = super().save(commit=False)
        teacher.set_password(self.cleaned_data['password'])  # Establecer la contraseña de manera segura
        if commit:
            teacher.save()  # Guarda el usuario en la base de datos
        return teacher
