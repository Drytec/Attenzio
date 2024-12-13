from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Session, Material, MaterialSession, Question, Option
from ..course.models import Course
from rest_framework import status
from .serializers import SessionSerializer, MaterialSerializer, QuestionSerializer, OptionSerializer


class ShowSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        session = get_object_or_404(Session, session_id=session_id)
        materials = Material.objects.filter(materialsession__session_id=session_id)
        material_data = [{'material_id': material.material_id, 'material_link': material.material_link} for material in materials]

        session_data = {
            'session_id': session.session_id,
            'session_name': session.session_name,
            'session_description': session.session_description,
            'session_date_start': session.session_date_start,
            'session_date_end': session.session_date_end,
            'materials': material_data
        }

        return Response(session_data, status=status.HTTP_200_OK)

class CreateSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        course = get_object_or_404(Course, course_id=course_id)

        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            new_session = serializer.save(course_id=course)
            return Response({
                'message': 'Sesión creada exitosamente',
                'session': SessionSerializer(new_session).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateMaterialView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id):
        session = get_object_or_404(Session, pk=session_id)

        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            new_material = serializer.save()
            MaterialSession.objects.create(session_id=session, material_id=new_material)
            return Response({
                'message': 'Material creado exitosamente',
                'material': MaterialSerializer(new_material).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id):
        session = get_object_or_404(Session, pk=session_id)

        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            new_question = serializer.save(session_id=session)
            return Response({
                'message': 'Pregunta creada exitosamente',
                'question': QuestionSerializer(new_question).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateOptionsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id, question_id):
        question = get_object_or_404(Question, pk=question_id)

        options_data = request.data.get('options', [])
        for option_data in options_data:
            serializer = OptionSerializer(data=option_data)
            if serializer.is_valid():
                serializer.save(question_id=question)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Opciones creadas exitosamente'}, status=status.HTTP_201_CREATED)

class ShowOptionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id, question_id):
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'detail': 'Permiso denegado'}, status=status.HTTP_403_FORBIDDEN)

        question = get_object_or_404(Question, pk=question_id)
        options = Option.objects.filter(question_id=question_id)

        options_data = OptionSerializer(options, many=True).data

        return Response({'options': options_data}, status=status.HTTP_200_OK)

class ShowQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'detail': 'Permiso denegado'}, status=status.HTTP_403_FORBIDDEN)

        session = get_object_or_404(Session, pk=session_id)

        questions = Question.objects.filter(session_id=session_id)

        questions_data = QuestionSerializer(questions, many=True).data

        # Devolver las preguntas en formato JSON
        return Response({'questions': questions_data, 'session': {
            'session_id': session.session_id,
            'session_name': session.session_name,
            'session_description': session.session_description,
            'session_date_start': session.session_date_start,
            'session_date_end': session.session_date_end,
        }}, status=status.HTTP_200_OK)