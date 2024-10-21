from django.urls import path, include
from .views import home, aula, exit, signup, register, login1, create_aula, aula_class,aula_online

urlpatterns = [
    path('',home, name='home'),
    path ('aula/',aula_class,name='aula'),
    path ('logout/',exit,name='exit'),
    path('signup/',signup,name='signup'),
    path('register/',register,name='register'),
    path('login1/',login1,name='login1'),
    path('aula/create/',create_aula,name='create_aula'),
    path('aula/online/',aula_online,name='aula_online'),


]
