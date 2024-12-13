from django.urls import path
from .views import create_course, show_course, get_courses, join_course

urlpatterns = [
    path('courses/', get_courses, name='get_courses'),
    path('create_course/', create_course, name='create_course'),
    path('join_course/', join_course, name=join_course),
    path('courses/c:<int:course_id>/', show_course, name='show_course'),
]
