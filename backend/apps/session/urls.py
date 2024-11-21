from django.urls import path, include
from .views import Session, exit, create_session, session_class, session_interactive
urlpatterns = [
    path ('session/', session_class,name='session'),
    path ('logout/', exit,name='exit'),
    path('sesion/create/', create_session,name='create_session'),
    path('sesion/<int:aula_id>/', session_interactive,name='session_online'),

]
