from django.urls import path, include
from .views import Session, exit, create_session, show_session, create_material, create_question, create_options, \
    report_view

urlpatterns = [
    path ('logout/', exit,name='exit'),
    path('create_session/<int:course_id>/', create_session, name='create_session'),
    path('create_material/', create_material, name='create_material'),
    path('create_question/', create_question, name='create_question'),
    path('create_options/', create_options, name='create_options'),
    path('s:<int:session_id>/', show_session, name='show_session'),
    path('create_session/', create_session, name='create_session'),
    path('report/<int:custom_user_id>/<int:course_id>/', report_view, name='report_view'),
]
