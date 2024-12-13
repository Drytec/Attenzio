from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginView(APIView):
    """
    Vista para manejar el inicio de sesión de un usuario.

    Método:
        POST: Valida los datos de inicio de sesión, autentica al usuario y devuelve una respuesta con el mensaje de éxito
              y los datos del usuario si las credenciales son correctas, o un error en caso contrario.

    Respuesta:
        - 200 OK: Si el inicio de sesión es exitoso, con los datos del usuario.
        - 400 Bad Request: Si las credenciales son incorrectas o el serializador es inválido.
    """

    def post(self, request):
        """
        Intenta autenticar a un usuario con los datos proporcionados (email y contraseña).

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene los datos de inicio de sesión.

        Respuesta:
            - 200 OK: Si las credenciales son correctas.
            - 400 Bad Request: Si las credenciales son incorrectas o los datos no son válidos.
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                return Response({
                    'message': 'Login exitoso',
                    'user': {
                        'email': user.email,
                        'full_name': user.full_name
                    }
                }, status=status.HTTP_200_OK)

            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    """
    Vista para manejar el cierre de sesión de un usuario autenticado.

    Método:
        POST: Cierra la sesión del usuario autenticado y devuelve un mensaje de éxito.

    Respuesta:
        - 200 OK: Si el cierre de sesión es exitoso.
        - 403 Forbidden: Si el usuario no está autenticado.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Cierra la sesión del usuario autenticado.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la sesión activa del usuario.

        Respuesta:
            - 200 OK: Si el cierre de sesión es exitoso.
        """
        logout(request)
        return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    """
    Vista para manejar el registro de un nuevo usuario.
    """

    def post(self, request):
        """
        Crea un nuevo usuario con los datos proporcionados en la solicitud.
        """
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response({
                'message': 'Registro exitoso',
                'user': {
                    'email': user.email,
                    'full_name': user.full_name,
                    'role': user.rol_id.name
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

