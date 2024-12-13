
from django.urls import path, include
from .views import Session, exit, create_session, course_sessions,session_interactive
urlpatterns = [
    path ('sessions/', course_sessions,name='course_sessions'),
    path ('logout/', exit,name='exit'),
    path('create_session/', create_session, name='create_session'),
    path('course/<int:aula_id>/', session_interactive, name='session_online'),

]
