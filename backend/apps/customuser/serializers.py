from rest_framework import serializers
from .models import CustomUser, Rol
from PIL import Image
import io
import base64

from rest_framework import serializers
from .models import CustomUser, Rol
import base64
from PIL import Image
import io

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer para registrar un nuevo usuario. Este serializer valida y procesa los datos
    proporcionados por el usuario al momento de registro, incluyendo la creación de un usuario
    y la asignación del rol según el tipo de usuario ('teacher' o 'student').
    """

    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=['student', 'teacher'], write_only=True)
    document = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=30, required=False)
    address = serializers.CharField(max_length=100, required=False)
    media = serializers.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name', 'phone', 'address', 'media', 'document', 'user_type']
        extra_kwargs = {
            'full_name': {'required': True},
            'document': {'required': True},
            'address': {'required': False},
            'media': {'required': False},
            'email': {'required': True},
            'password': {'required': True},
            'phone': {'required': False},
        }

    def create(self, validated_data):
        """
        Crea un nuevo usuario y guarda la imagen en base64 si es proporcionada.
        """
        user_type = validated_data.pop('user_type')
        media = validated_data.pop('media', None)

        if media:
            image_base64 = self.image_to_base64(media)
            validated_data['media'] = image_base64

        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)

        if user_type == 'teacher':
            rol = Rol.objects.get(rol_id=1)
        else:
            rol = Rol.objects.get(rol_id=2)

        user.rol_id = rol
        user.save()

        return user

    def image_to_base64(self, image):
        """
        Convierte una imagen a una cadena codificada en Base64.
        """
        image_file = io.BytesIO()
        img = Image.open(image)
        img.save(image_file, format=img.format)
        image_file.seek(0)
        return base64.b64encode(image_file.read()).decode('utf-8')


class LoginSerializer(serializers.Serializer):
    """
    Serializer para el proceso de login de un usuario. Este serializer valida las credenciales
    de inicio de sesión (correo electrónico y contraseña) y asigna un rol al usuario durante
    el proceso de autenticación.

    Campos:
        - email (str): El correo electrónico del usuario.
        - password (str): La contraseña del usuario.

    Métodos:
        - `create()`: Valida las credenciales del usuario y asigna el rol apropiado.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Crea un usuario para iniciar sesión. El rol es asignado dependiendo del tipo de usuario
        ('teacher' o 'student').

        Parámetros:
            validated_data (dict): Los datos validados del formulario de inicio de sesión.

        Retorna:
            user (CustomUser): El objeto de usuario autenticado.
        """
        user_type = validated_data.pop('user_type')

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])

        if user_type == 'teacher':
            rol = Rol.objects.get(rol_id=1)
        else:
            rol = Rol.objects.get(rol_id=2)

        user.rol_id = rol
        user.save()

        return user