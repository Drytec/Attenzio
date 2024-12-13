from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Session, Material, MaterialSession, Question, Option
from ..course.models import Course
from rest_framework import status
from .serializers import SessionSerializer, MaterialSerializer, QuestionSerializer, OptionSerializer

class ShowSessionView(APIView):
    """
    Vista para obtener los detalles de una sesión específica.

    Este endpoint requiere que el usuario esté autenticado. Devuelve los detalles de la sesión
    (nombre, descripción, fechas de inicio y fin) y los materiales asociados con ella.

    Permisos:
        - Requiere autenticación.

    Parámetros de la URL:
        - session_id: El ID de la sesión que se desea obtener.

    Respuesta:
        - 200 OK: Si la sesión se encuentra, retorna los detalles de la sesión y los materiales.
        - 404 Not Found: Si no se encuentra la sesión con el ID proporcionado.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        # Obtiene la sesión y sus materiales asociados
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
    """
    Vista para crear una nueva sesión dentro de un curso específico.

    Este endpoint requiere que el usuario esté autenticado y proporcione los detalles de la sesión.

    Permisos:
        - Requiere autenticación.

    Parámetros de la URL:
        - course_id: El ID del curso donde se debe crear la sesión.

    Respuesta:
        - 201 Created: Si la sesión se crea correctamente, retorna los detalles de la nueva sesión.
        - 400 Bad Request: Si los datos enviados son inválidos.
    """

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
    """
    Vista para crear un nuevo material asociado a una sesión.

    Este endpoint requiere que el usuario esté autenticado y que se le proporcione el ID de la sesión.

    Permisos:
        - Requiere autenticación.

    Parámetros de la URL:
        - session_id: El ID de la sesión donde se debe crear el material.

    Respuesta:
        - 201 Created: Si el material se crea correctamente, retorna los detalles del nuevo material.
        - 400 Bad Request: Si los datos enviados son inválidos.
    """

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
    """
    Vista para crear una nueva pregunta dentro de una sesión.

    Este endpoint requiere que el usuario esté autenticado y proporcione los detalles de la pregunta.

    Permisos:
        - Requiere autenticación.

    Parámetros de la URL:
        - session_id: El ID de la sesión donde se debe crear la pregunta.

    Respuesta:
        - 201 Created: Si la pregunta se crea correctamente, retorna los detalles de la nueva pregunta.
        - 400 Bad Request: Si los datos enviados son inválidos.
    """

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
    """
    Vista para crear opciones de respuesta para una pregunta específica dentro de una sesión.

    Este endpoint requiere que el usuario esté autenticado y proporcione las opciones asociadas
    a una pregunta.

    Permisos:
        - Requiere autenticación.

    Parámetros de la URL:
        - session_id: El ID de la sesión donde se encuentra la pregunta.
        - question_id: El ID de la pregunta a la que se le añadirán las opciones.

    Respuesta:
        - 201 Created: Si las opciones se crean correctamente, retorna un mensaje de éxito.
        - 400 Bad Request: Si los datos enviados son inválidos.
    """

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
    """
    Vista para obtener las opciones asociadas a una pregunta en una sesión específica.

    Este endpoint requiere que el usuario esté autenticado y tenga permisos de profesor o administrador.

    Permisos:
        - Requiere autenticación.
        - Solo accesible por usuarios con rol de Profesor o Administrador.

    Parámetros de la URL:
        - session_id: El ID de la sesión donde se encuentra la pregunta.
        - question_id: El ID de la pregunta de la cual se desean obtener las opciones.

    Respuesta:
        - 200 OK: Si se encuentran las opciones asociadas a la pregunta, se retornan.
        - 403 Forbidden: Si el usuario no tiene permisos para acceder a las opciones.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, session_id, question_id):
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'detail': 'Permiso denegado'}, status=status.HTTP_403_FORBIDDEN)

        options = Option.objects.filter(question_id=question_id)

        options_data = OptionSerializer(options, many=True).data

        return Response({'options': options_data}, status=status.HTTP_200_OK)

class ShowQuestionsView(APIView):
    """
    Vista para obtener las preguntas asociadas a una sesión específica.

    Este endpoint requiere que el usuario esté autenticado y tenga permisos de profesor o administrador.

    Permisos:
        - Requiere autenticación.
        - Solo accesible por usuarios con rol de Profesor o Administrador.

    Parámetros de la URL:
        - session_id: El ID de la sesión de la cual se desean obtener las preguntas.

    Respuesta:
        - 200 OK: Si se encuentran preguntas asociadas a la sesión, se retornan.
        - 403 Forbidden: Si el usuario no tiene permisos para acceder a las preguntas.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'detail': 'Permiso denegado'}, status=status.HTTP_403_FORBIDDEN)

        session = get_object_or_404(Session, pk=session_id)

        questions = Question.objects.filter(session_id=session_id)

        questions_data = QuestionSerializer(questions, many=True).data

        return Response({'questions': questions_data, 'session': {
            'session_id': session.session_id,
            'session_name': session.session_name,
            'session_description': session.session_description,
            'session_date_start': session.session_date_start,
            'session_date_end': session.session_date_end,
        }}, status=status.HTTP_200_OK)