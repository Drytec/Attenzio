from django.urls import path
from .views import home, user_login_view, user_singup_view, select_user_type_view,logout_view

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', user_login_view, name='login'),
    path('select_user_type/', select_user_type_view, name='select_user_type'),
    path('signup/', user_singup_view, name='signup'),

    path('api/teacher-register/', TeacherRegisterAPIView.as_view(), name='teacher_register'),
    path('api/student-register/', StudentRegisterAPIView.as_view(), name='student_register'),
]
