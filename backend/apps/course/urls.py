from django.urls import path
from .views import *

urlpatterns = [
    path('student_courses/', StudentCoursesView.as_view(), name='student_courses'),
    path('teacher_courses/', TeacherCoursesView.as_view(), name='teacher_courses'),
    path('admin_courses/', AdminCoursesView.as_view(), name='admin_courses'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
    path('c:<int:course_id>/', ShowCourseView.as_view(), name='show_course'),
]
