from django.urls import path, include

from .views import home, user_login_view, user_singup_view, select_user_type_view

urlpatterns = [
    path('',home, name='home'),
    path ('logout/', exit, name='exit'),
    path('login/', user_login_view, name='login'),
    path('select_user_type/', select_user_type_view, name='select-type'),
    path('signup/', user_singup_view, name='signup'),
]
