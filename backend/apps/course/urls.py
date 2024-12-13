from django.urls import path
from .views import *

urlpatterns = [
    path('get_courses/', GetCoursesView.as_view(), name='get_courses'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
    path('c:<int:course_id>/', ShowCourseView.as_view(), name='show_course'),
]
