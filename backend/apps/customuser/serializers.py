from rest_framework import serializers
from .models import CustomUser, Rol
from PIL import Image
import io
import base64

class RegisterSerializer(serializers.ModelSerializer):
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
        media = validated_data.pop('media', None)
        if media:
            image_base64 = self.image_to_base64(media)
            validated_data['media'] = image_base64

        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
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


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['rol_id', 'rol_name']

class CustomUserSerializer(serializers.ModelSerializer):
    rol_id = RolSerializer()

    class Meta:
        model = CustomUser
        fields = ['custom_user_id', 'full_name', 'document', 'address', 'email', 'phone', 'rol_id', 'is_active']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
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
