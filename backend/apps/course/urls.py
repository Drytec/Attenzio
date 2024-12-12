from django.urls import path, include
from .views import create_course, teacher_courses, show_course, student_courses, admin_courses

urlpatterns = [
    path ('teacher_courses', teacher_courses, name='teacher_courses'),
    path ('student_courses', student_courses, name='student_courses'),
    path ('admin_courses', admin_courses, name='admin_courses'),
    path ('logout/', exit, name='exit'),
    path('create_course/', create_course, name='create_course'),
    path('c:<int:course_id>/', show_course, name='show_course'),
]