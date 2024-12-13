from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUserCourse, Course
from .serializers import CourseSerializer, CustomUserCourseSerializer
from ..session.models import Session
from ..session.serializers import SessionSerializer

class StudentCoursesView(APIView):
    """
    Vista que devuelve los cursos asociados a un estudiante.

    Requiere que el usuario esté autenticado y sea un estudiante.

    Respuesta:
        - 200 OK: Devuelve una lista de cursos y los profesores asociados.
        - 403 Forbidden: Si el usuario no es un estudiante.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtiene la lista de cursos del estudiante autenticado.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la información del usuario autenticado.

        Respuesta:
            - Response: Devuelve una lista de cursos con sus profesores si el usuario es un estudiante.
        """
        if not request.user.isStudent:
            return Response({'error': 'Acción no permitida'}, status=403)

        course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list(
            'course_id', flat=True)
        courses = Course.objects.filter(course_id__in=course_ids)
        serializer = CourseSerializer(courses, many=True)

        course_teachers = []
        for course in courses:
            teacher = CustomUserCourse.objects.filter(course_id=course.course_id,
                                                      custom_user_id__is_teacher=True).select_related(
                'custom_user_id').first()
            course_teachers.append(teacher.custom_user_id if teacher else None)

        return Response({'courses': serializer.data, 'teachers': course_teachers})


class TeacherCoursesView(APIView):
    """
    Vista que devuelve los cursos asociados a un profesor.

    Requiere que el usuario esté autenticado y sea un profesor.

    Respuesta:
        - 200 OK: Devuelve una lista de cursos.
        - 403 Forbidden: Si el usuario no es un profesor.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtiene la lista de cursos del profesor autenticado.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la información del usuario autenticado.

        Respuesta:
            - Response: Devuelve una lista de cursos si el usuario es un profesor.
        """
        if not request.user.isTeacher:
            return Response({'error': 'Acción no permitida'}, status=403)

        # Obtener cursos asociados al profesor
        course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list(
            'course_id', flat=True)
        courses = Course.objects.filter(course_id__in=course_ids)
        serializer = CourseSerializer(courses, many=True)

        return Response({'courses': serializer.data})


class AdminCoursesView(APIView):
    """
    Vista que devuelve los cursos asociados a un administrador.

    Requiere que el usuario esté autenticado y sea un administrador.

    Respuesta:
        - 200 OK: Devuelve una lista de cursos.
        - 403 Forbidden: Si el usuario no es un administrador.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtiene la lista de cursos del administrador autenticado.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la información del usuario autenticado.

        Respuesta:
            - Response: Devuelve una lista de cursos si el usuario es un administrador.
        """
        if not request.user.isAdmin:
            return Response({'error': 'Acción no permitida'}, status=403)

        # Obtener cursos asociados al administrador
        course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list(
            'course_id', flat=True)
        courses = Course.objects.filter(course_id__in=course_ids)
        serializer = CourseSerializer(courses, many=True)

        return Response({'courses': serializer.data})


class CreateCourseView(APIView):
    """
    Vista para crear un nuevo curso. Solo accesible por profesores y administradores.

    Requiere que el usuario esté autenticado y sea un profesor o administrador.

    Respuesta:
        - 201 Created: Si el curso fue creado exitosamente.
        - 403 Forbidden: Si el usuario no es un profesor o administrador.
        - 400 Bad Request: Si hay errores en los datos proporcionados.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Crea un nuevo curso.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene los datos del curso a crear.

        Respuesta:
            - Response: Mensaje de éxito si el curso fue creado exitosamente, o los errores si no lo fue.
        """
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'error': 'Acción no permitida'}, status=403)

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            CustomUserCourse.objects.create(custom_user_id=request.user, course_id=course)
            return Response({'message': 'Curso creado exitosamente', 'course': serializer.data}, status=201)

        return Response({'errors': serializer.errors}, status=400)


class ShowCourseView(APIView):
    """
    Vista para mostrar detalles de un curso específico.

    Requiere que el usuario esté autenticado.

    Respuesta:
        - 200 OK: Devuelve los detalles del curso, las sesiones y el profesor asociado.
        - 404 Not Found: Si el curso no existe.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        """
        Obtiene los detalles de un curso específico.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la información del usuario autenticado.
            course_id (int): ID del curso.

        Respuesta:
            - Response: Devuelve los detalles del curso, las sesiones y el profesor si existe.
        """
        course = get_object_or_404(Course, pk=course_id)
        sessions = Session.objects.filter(course_id=course_id)

        custom_user_course = CustomUserCourse.objects.filter(course_id=course_id).first()
        teacher = custom_user_course.custom_user_id if custom_user_course else None

        course_data = CourseSerializer(course).data
        sessions_data = SessionSerializer(sessions, many=True).data
        teacher_data = CustomUserCourseSerializer(teacher).data if teacher else None

        return Response({
            'course': course_data,
            'sessions': sessions_data,
            'teacher': teacher_data
        }, status=status.HTTP_200_OK)

class JoinCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        """
        Permite a un estudiante unirse a un curso mediante el course_id.

        Parámetros:
            request (Request): Objeto de solicitud HTTP que contiene la información del usuario autenticado.
            course_id (int): ID del curso al que se desea unir el estudiante.

        Respuesta:
            - 200 OK: Si el estudiante se une al curso exitosamente.
            - 403 Forbidden: Si el usuario no es un estudiante.
            - 404 Not Found: Si el curso no existe.
        """
        if not request.user.isStudent:
            return Response({'error': 'Acción no permitida. Solo los estudiantes pueden unirse a un curso.'}, status=403)

        course = get_object_or_404(Course, pk=course_id)

        if CustomUserCourse.objects.filter(custom_user_id=request.user, course_id=course).exists():
            return Response({'error': 'Ya estás inscrito en este curso.'}, status=400)

        CustomUserCourse.objects.create(custom_user_id=request.user, course_id=course)

        return Response({'message': 'Te has unido al curso exitosamente.'}, status=200)