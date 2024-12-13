from django.urls import path
from .views import StudentCoursesView, TeacherCoursesView, AdminCoursesView, CreateCourseView

urlpatterns = [
    path('api/student_courses/', StudentCoursesView.as_view(), name='student_courses'),
    path('api/teacher_courses/', TeacherCoursesView.as_view(), name='teacher_courses'),
    path('api/admin_courses/', AdminCoursesView.as_view(), name='admin_courses'),
    path('api/create_course/', CreateCourseView.as_view(), name='create_course'),
]
