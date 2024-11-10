from django.urls import path, include
from .views import sesion, exit, create_sesion, sesion_class, sesion_interactive
urlpatterns = [
    path ('sesion/',sesion_class,name='sesion'),
    path ('logout/',exit,name='exit'),
    path('sesion/create/',create_sesion,name='create_sesion'),
    path('sesion/<int:aula_id>/',sesion_interactive,name='sesion_online'),

]
