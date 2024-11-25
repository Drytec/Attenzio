from django.urls import path, include
from .views import Session, exit, create_session, show_session
urlpatterns = [
    path ('logout/', exit,name='exit'),
    path('create_session/', create_session, name='create_session'),
    path('s:<int:aula_id>/', show_session, name='show_session'),
]
