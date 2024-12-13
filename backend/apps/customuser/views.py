from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginView(APIView):
    """
    Vista para manejar el inicio de sesión de un usuario.

    Método:
        POST: Valida los datos de inicio de sesión, autentica al usuario y devuelve un JWT si las credenciales son correctas.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Intenta autenticar a un usuario con los datos proporcionados (email y contraseña).

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene los datos de inicio de sesión.

        Respuesta:
            - 200 OK: Si las credenciales son correctas, con un JWT.
            - 400 Bad Request: Si las credenciales son incorrectas o los datos no son válidos.
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    'message': 'Login exitoso',
                    'user': {
                        'email': user.email,
                        'full_name': user.full_name
                    },
                    'access_token': str(access_token),
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
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registra a un nuevo usuario y genera un token JWT para él.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene los datos del nuevo usuario.

        Respuesta:
            - 201 Created: Si el registro es exitoso, con los datos del usuario y el JWT.
            - 400 Bad Request: Si los datos no son válidos.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'message': 'Registro exitoso',
                'user': {
                    'email': user.email,
                    'full_name': user.full_name
                },
                'access_token': access_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


