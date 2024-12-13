from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager

media = models.ImageField(upload_to='uploads/', blank=True, null=True)

class CustomUserManager(BaseUserManager):
    """
    Manager personalizado para el modelo `CustomUser`. Proporciona métodos adicionales
    para la gestión de usuarios, como la recuperación de usuarios por su clave natural (email).
    """

    def get_by_natural_key(self, email):
        """
        Obtiene un usuario por su dirección de correo electrónico.

        Parámetros:
            email (str): El correo electrónico del usuario a recuperar.

        Retorna:
            CustomUser: El usuario que tiene el correo electrónico proporcionado.
        """
        return self.get(email=email)


class Rol(models.Model):
    """
    Modelo que representa los roles de los usuarios en el sistema (por ejemplo: Profesor, Estudiante, Administrador).

    Atributos:
        - rol_id (int): Identificador único del rol.
        - rol_name (str): Nombre del rol (por ejemplo, 'Profesor', 'Estudiante', 'Administrador').

    Esta tabla no es gestionada por Django (no se creará ni modificará automáticamente).
    """
    rol_id = models.IntegerField(primary_key=True)
    rol_name = models.CharField(max_length=100)

    class Meta:
        db_table = "rol"
        managed = False

    def __str__(self):
        """
        Retorna una representación en cadena del rol.
        """
        return f'{self.rol_id}'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado que extiende `AbstractBaseUser` y `PermissionsMixin`.
    Este modelo es utilizado para la autenticación de usuarios y define campos adicionales
    como nombre completo, documento, dirección y rol del usuario.

    Atributos:
        - custom_user_id (int): Identificador único del usuario.
        - full_name (str): Nombre completo del usuario.
        - document (str): Número de documento único del usuario.
        - address (str): Dirección del usuario.
        - media (str): Campo de texto para almacenar la URL de la imagen de perfil.
        - email (str): Correo electrónico único del usuario, usado como nombre de usuario.
        - password (str): Contraseña del usuario.
        - phone (str): Número de teléfono del usuario.
        - rol_id (ForeignKey): Relación con el modelo `Rol`, define el rol del usuario.
        - validated (bool): Indica si el usuario está validado.
        - last_login (datetime): Fecha y hora del último inicio de sesión del usuario.
        - is_superuser (bool): Indica si el usuario es un superusuario.
        - is_staff (bool): Indica si el usuario es un miembro del personal.
        - is_active (bool): Indica si el usuario está activo.
        - date_joined (datetime): Fecha y hora en que el usuario se registró.

    Propiedades:
        - isTeacher (bool): Retorna `True` si el usuario tiene rol de 'Profesor'.
        - isStudent (bool): Retorna `True` si el usuario tiene rol de 'Estudiante'.
        - isAdmin (bool): Retorna `True` si el usuario tiene rol de 'Administrador'.

    Métodos:
        - get_by_natural_key: Método que permite obtener un usuario por su correo electrónico.
    """

    custom_user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, null=True)
    media = models.TextField(blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=30, blank=True)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')
    validated = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    class Meta:
        db_table = 'customuser'
        managed = False

    def __str__(self):
        """
        Retorna el nombre completo del usuario como representación en cadena.
        """
        return self.full_name

    @property
    def isTeacher(self):
        """
        Propiedad que retorna `True` si el usuario tiene el rol de 'Profesor' (rol_id == 1).
        """
        return self.rol_id_id == 1

    @property
    def isStudent(self):
        """
        Propiedad que retorna `True` si el usuario tiene el rol de 'Estudiante' (rol_id == 2).
        """
        return self.rol_id_id == 2

    @property
    def isAdmin(self):
        """
        Propiedad que retorna `True` si el usuario tiene el rol de 'Administrador' (rol_id == 3).
        """
        return self.rol_id_id == 3

    def get_by_natural_key(self, email):
        """
        Recupera un usuario por su dirección de correo electrónico.

        Parámetros:
            email (str): El correo electrónico del usuario a recuperar.

        Retorna:
            CustomUser: El usuario con el correo electrónico proporcionado.
        """
        return self.objects.get(email=email)
