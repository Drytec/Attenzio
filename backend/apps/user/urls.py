from django.urls import path, include

from .views import home, login, teacher_login_view, teacher_singup_view

urlpatterns = [
    path('',home, name='home'),
    path ('teacher/logout/', exit, name='exit'),
    path('teacher/login/', teacher_login_view, name='login'),
    path('teacher/signup/', teacher_singup_view, name='signup'),
]
