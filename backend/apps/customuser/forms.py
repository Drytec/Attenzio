from django import forms
from django.utils.crypto import get_random_string
from .models import CustomUser, Rol

class BaseRegisterForm(forms.ModelForm):
    """
    Formulario base para el registro de usuarios. Este formulario incluye campos comunes
    como documento, nombre completo, teléfono, email, dirección, foto de perfil y contraseña.

    Campos:
    - document: Documento de identidad único del usuario.
    - full_name: Nombre completo del usuario.
    - phone: Número de teléfono del usuario.
    - email: Correo electrónico del usuario.
    - address: Dirección del usuario.
    - media: Enlace a la foto de perfil o recurso asociado.
    - password: Contraseña del usuario (input oculto).

    Métodos:
    - clean_document: Valida que el documento no esté repetido.
    - clean_email: Valida que el correo electrónico no esté repetido.
    """
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'phone', 'email', 'address', 'media', 'password']
        labels = {
            'document': 'Documento',
            'full_name': 'Nombre Completo',
            'phone': 'Celular',
            'email': 'Email',
            'address': 'Dirección',
            'media': 'Link a la foto',
        }

    def clean_document(self):
        """
        Valida que el documento del usuario sea único.

        Si el documento ya existe en la base de datos, lanza una excepción de validación.

        Retorna:
        - El documento proporcionado si es válido.

        Excepción:
        - Validación si el documento ya está registrado.
        """
        document = self.cleaned_data.get('document')
        if CustomUser.objects.filter(document=document).exists():
            raise forms.ValidationError('El documento ya existe. Por favor, utiliza otro.')
        return document

    def clean_email(self):
        """
        Valida que el correo electrónico del usuario sea único.

        Si el correo ya existe en la base de datos, lanza una excepción de validación.

        Retorna:
        - El correo electrónico proporcionado si es válido.

        Excepción:
        - Validación si el correo electrónico ya está registrado.
        """
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya existe. Por favor, utiliza otro.')
        return email

class TeacherRegisterForm(BaseRegisterForm):
    """
    Formulario para el registro de un usuario con el rol de 'Profesor'.

    Este formulario utiliza el formulario base `BaseRegisterForm` y asigna el rol de Profesor
    al usuario al momento de guardarlo.

    Métodos:
    - save: Guarda el usuario y asigna el rol de Profesor (rol_id = 1).
    """
    def save(self, commit=True):
        """
        Guarda el usuario con el rol de Profesor.

        Asigna el rol de Profesor antes de guardar el usuario.

        Parámetros:
        - commit: Si es True, guarda el usuario en la base de datos.

        Retorna:
        - El usuario recién guardado.
        """
        user = super().save(commit=False)
        rol = Rol.objects.get(rol_id=1)  # Obtiene el rol de Profesor
        user.rol_id = rol
        if commit:
            user.save()
        return user

class StudentRegisterForm(BaseRegisterForm):
    """
    Formulario para el registro de un usuario con el rol de 'Estudiante'.

    Este formulario utiliza el formulario base `BaseRegisterForm` y asigna el rol de Estudiante
    al usuario. Además, genera un nombre de usuario aleatorio y valida que el código de estudiante
    sea único.

    Campos adicionales:
    - document: Se etiqueta como 'Código de Estudiante' en lugar de 'Documento'.
    - media: Se etiqueta como 'Link al tabulado' en lugar de 'Link a la foto'.

    Métodos:
    - save: Guarda el usuario, asigna el rol de Estudiante (rol_id = 2), valida el código de estudiante,
      genera un nombre de usuario aleatorio y asigna el estado de validado.
    - clean_document: Valida que el código de estudiante sea único.
    """
    class Meta(BaseRegisterForm.Meta):
        labels = {
            **BaseRegisterForm.Meta.labels,
            'document': 'Código de Estudiante',
            'media': 'Link al tabulado',
        }

    def save(self, commit=True):
        """
        Guarda el usuario con el rol de Estudiante y genera un nombre de usuario aleatorio.

        Asigna el rol de Estudiante antes de guardar el usuario, genera un nombre de usuario aleatorio
        y marca al usuario como validado.

        Parámetros:
        - commit: Si es True, guarda el usuario en la base de datos.

        Retorna:
        - El usuario recién guardado.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Establece la contraseña encriptada
        user.username = f"{user.full_name}{get_random_string(length=5)}"  # Genera nombre de usuario aleatorio
        user.validate = True  # Marca al usuario como validado
        user.rol_id = Rol.objects.get(rol_id=2)  # Asigna el rol de Estudiante

        if commit:
            user.save()
        return user

    def clean_document(self):
        """
        Valida que el código de estudiante sea único.

        Si el código de estudiante ya existe, lanza una excepción de validación.

        Retorna:
        - El código de estudiante proporcionado si es válido.

        Excepción:
        - Validación si el código de estudiante ya está registrado.
        """
        document = self.cleaned_data.get('document')
        if CustomUser.objects.filter(document=document).exists():
            raise forms.ValidationError('El código ya existe. Por favor, utiliza otro.')
        return document



