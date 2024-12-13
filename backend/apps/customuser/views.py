from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .serializers import TeacherRegisterSerializer, StudentRegisterSerializer

class HomeAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Welcome to the API Home"}, status=status.HTTP_200_OK)

class SelectUserTypeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_type = request.data.get('user_type')
        if user_type in ['student', 'teacher']:
            return Response({"redirect_url": f"/signup/?type={user_type}"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

class UserSignupAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_type = request.query_params.get('type')

        if user_type == 'teacher':
            serializer = TeacherRegisterSerializer()
        else:
            serializer = StudentRegisterSerializer()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_type = request.query_params.get('type')

        if user_type == 'teacher':
            serializer_class = TeacherRegisterSerializer
        else:
            serializer_class = StudentRegisterSerializer

        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Both fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Uncomment this block if validation logic is needed:
        # if not user.validate:
        #     return Response({"error": "Your account needs to be validated by an administrator."}, status=status.HTTP_403_FORBIDDEN)

        login(request, user)
        return Response({"message": "Login successful", "redirect_url": "/home"}, status=status.HTTP_200_OK)

