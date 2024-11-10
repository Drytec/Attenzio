from django.urls import path, include
from .views import sesion, exit, create_sesion, sesion_class, sesion_interactive

urlpatterns = [
    path ('sesion/',sesion_class,name='aula'),
    path ('logout/',exit,name='exit'),
    path('sesion/create/',create_sesion,name='create_aula'),
    path('sesion/<int:aula_id>/',sesion_interactive,name='aula_online'),

]
