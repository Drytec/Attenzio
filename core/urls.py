from django.urls import path, include
from .views import home,teachers,exit
urlpatterns = [
    path('',home, name='home'),
    path ('teachers/',teachers,name='teachers'),
    path ('logout/',exit,name='exit'),
]
