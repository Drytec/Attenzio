from rest_framework import serializers
from .models import CustomUser, Rol

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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=['student', 'teacher'], write_only=True)  # Selección de tipo de usuario
    document = serializers.CharField(max_length=20)  # Documento obligatorio
    phone = serializers.CharField(max_length=30, required=False)  # Teléfono opcional
    address = serializers.CharField(max_length=100, required=False)  # Dirección opcional
    media = serializers.ImageField(required=False)  # Foto opcional

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name', 'phone', 'address', 'media', 'document', 'user_type']
        extra_kwargs = {
            'full_name': {'required': True},
            'document': {'required': True},
            'address': {'required': True},
            'media': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
            'phone': {'required': True},
        }

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
