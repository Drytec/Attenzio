from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import CustomUser, Rol

class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'phone', 'email', 'address', 'media', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            **validated_data
        )
        rol = Rol.objects.get(rol_id=1)
        user.rol_id = rol

        user.set_password(validated_data['password'])
        user.save()

        return user

class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['document', 'full_name', 'phone', 'email', 'address', 'media', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            **validated_data
        )
        user.username = f"{user.full_name}{get_random_string(length=5)}"
        user.validate = True

        rol = Rol.objects.get(rol_id=2)
        user.rol_id = rol

        user.set_password(validated_data['password'])
        user.save()

        return user