from django.urls import path, include

from .views import home, login, student_login_view, student_singup_view

urlpatterns = [
    path('',home, name='home'),
    path ('logout/', exit,name='exit'),
    path('login/', student_login_view, name='login'),
    path('signup/', student_singup_view, name='signup'),
]