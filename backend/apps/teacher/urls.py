from django.urls import path, include

from .views import home, register, login1, signup

urlpatterns = [
    path('',home, name='home'),
    path ('logout/',exit,name='exit'),
    path('register/',register,name='register'),
    path('login1/',login1,name='login1'),
    path('signup/',signup,name='signup'),

]
