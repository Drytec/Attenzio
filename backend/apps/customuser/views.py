from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
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
                    'access_token': access_token,
                }, status=status.HTTP_200_OK)

            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response({
                'message': 'Registro exitoso',
                'user': {
                    'email': user.email,
                    'full_name': user.full_name
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Bienvenido a la página de inicio'}, status=status.HTTP_200_OK)
