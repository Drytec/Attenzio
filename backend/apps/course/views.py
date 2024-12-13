from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUserCourse, Course
from .serializers import CourseSerializer


class StudentCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.isTeacher:
            return Response({'error': 'Acción no permitida'}, status=403)

        course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list(
            'course_id', flat=True)
        courses = Course.objects.filter(course_id__in=course_ids)
        serializer = CourseSerializer(courses, many=True)

        return Response({'courses': serializer.data})


class AdminCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.isAdmin:
            return Response({'error': 'Acción no permitida'}, status=403)

        course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list(
            'course_id', flat=True)
        courses = Course.objects.filter(course_id__in=course_ids)
        serializer = CourseSerializer(courses, many=True)

        return Response({'courses': serializer.data})


class CreateCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.isTeacher and not request.user.isAdmin:
            return Response({'error': 'Acción no permitida'}, status=403)

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            CustomUserCourse.objects.create(custom_user_id=request.user, course_id=course)
            return Response({'message': 'Curso creado exitosamente', 'course': serializer.data}, status=201)

        return Response({'errors': serializer.errors}, status=400)
