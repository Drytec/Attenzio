from django import forms
from django.utils.crypto import get_random_string

from .models import CustomUser
from apps.rol.models import Rol

class BaseRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'email', 'address', 'media', 'password']
        labels = {
            'document': 'Documento',
            'full_name': 'Nombre Completo',
            'email': 'Email',
            'address': 'Dirección',
            'media': 'Foto',
        }

    def clean_document(self):
        document = self.cleaned_data.get('document')
        if CustomUser.objects.filter(document=document).exists():
            raise forms.ValidationError('El documento ya existe. Por favor, utiliza otro.')
        return document

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya existe. Por favor, utiliza otro.')
        return email


class StudentRegisterForm(BaseRegisterForm):
    class Meta(BaseRegisterForm.Meta):
        labels = {
            **BaseRegisterForm.Meta.labels,
            'media': 'Tabulado',
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = f"{user.full_name}{get_random_string(length=5)}"

        user.validate = True
        user.rol_id = 2

        if commit:
            user.save()
        return user


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        teacher_role = Rol.objects.get(rol_name='teacher')
        user.rol_id = teacher_role

        if commit:
            user.save()
        return user

class TeacherRegisterForm(BaseRegisterForm):
    class Meta(BaseRegisterForm.Meta):
        labels = {
            **BaseRegisterForm.Meta.labels,
            'media': 'Foto',
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = f"{user.full_name}{get_random_string(length=5)}"

        user.validate = False
        user.rol_id = 1

        if commit:
            user.save()
        return user
