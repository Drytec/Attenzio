from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Gestor personalizado para el modelo CustomUser.

    Este gestor permite obtener un usuario mediante su correo electrónico como clave natural.
    """
    def get_by_natural_key(self, email):
        """
        Obtiene un usuario usando su correo electrónico como clave natural.

        Parámetros:
        - email: El correo electrónico del usuario que se busca.

        Retorna:
        - El objeto CustomUser correspondiente al correo electrónico proporcionado.
        """
        return self.get(email=email)

class Rol(models.Model):
    """
    Modelo que representa un rol de usuario.

    Campos:
    - rol_id: Identificador único para el rol.
    - rol_name: Nombre del rol (ej. 'Estudiante', 'Profesor', 'Administrador').

    La tabla se maneja manualmente (`managed = False`) y no se gestiona automáticamente por Django.
    """
    rol_id = models.IntegerField(primary_key=True)
    rol_name = models.CharField(max_length=100)

    class Meta:
        db_table = "rol"
        managed = False

    def __str__(self):
        return f'{self.rol_id}'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modelo personalizado para el usuario en el sistema.

    Campos:
    - custom_user_id: Identificador único del usuario.
    - full_name: Nombre completo del usuario.
    - document: Documento de identificación único.
    - address: Dirección del usuario.
    - media: Enlace a una imagen de perfil o recurso asociado.
    - email: Correo electrónico único del usuario.
    - password: Contraseña cifrada del usuario.
    - phone: Número de teléfono del usuario.
    - rol_id: Relación con el rol asignado al usuario (Estudiante, Profesor, Administrador).
    - validated: Indica si la cuenta ha sido validada por un administrador.
    - last_login: Fecha y hora del último inicio de sesión.
    - is_superuser: Indica si el usuario es superusuario.
    - is_staff: Indica si el usuario es miembro del personal administrativo.
    - is_active: Indica si la cuenta del usuario está activa.
    - date_joined: Fecha y hora en que el usuario se unió al sistema.

    Métodos:
    - isTeacher: Propiedad que devuelve True si el rol del usuario es Profesor.
    - isStudent: Propiedad que devuelve True si el rol del usuario es Estudiante.
    - isAdmin: Propiedad que devuelve True si el rol del usuario es Administrador.
    - get_by_natural_key: Método que obtiene un usuario por su correo electrónico.
    """
    custom_user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, null=True)
    media = models.CharField(max_length=300, blank=True)
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

    # Campos requeridos para la autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    class Meta:
        db_table = 'customuser'
        managed = False

    def __str__(self):
        return self.full_name

    @property
    def isTeacher(self):
        """
        Propiedad que indica si el usuario tiene el rol de Profesor.

        Retorna:
        - True si el rol del usuario es Profesor (rol_id = 1).
        - False en cualquier otro caso.
        """
        return self.rol_id_id == 1

    @property
    def isStudent(self):
        """
        Propiedad que indica si el usuario tiene el rol de Estudiante.

        Retorna:
        - True si el rol del usuario es Estudiante (rol_id = 2).
        - False en cualquier otro caso.
        """
        return self.rol_id_id == 2

    @property
    def isAdmin(self):
        """
        Propiedad que indica si el usuario tiene el rol de Administrador.

        Retorna:
        - True si el rol del usuario es Administrador (rol_id = 3).
        - False en cualquier otro caso.
        """
        return self.rol_id_id == 3

    def get_by_natural_key(self, email):
        """
        Obtiene un usuario por su correo electrónico.

        Parámetros:
        - email: El correo electrónico del usuario.

        Retorna:
        - El objeto CustomUser correspondiente al correo electrónico proporcionado.
        """
        return self.objects.get(email=email)
