from django.urls import path, include

from .views import home, login, teacher_login_view, teacher_singup_view

urlpatterns = [
    path('',home, name='home'),
    path ('logout/', exit, name='exit'),
    path('login/', teacher_login_view, name='login'),
    path('signup/', teacher_singup_view, name='signup'),
]
