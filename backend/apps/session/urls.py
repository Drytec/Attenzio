from django.urls import path, include
from .views import Session, exit, create_session, course_sessions, show_session
urlpatterns = [
    path ('sessions/', course_sessions,name='course_sessions'),
    path ('logout/', exit,name='exit'),
    path('create_session/', create_session, name='create_session'),
    path('s:<int:aula_id>/', show_session, name='session_online'),

]
