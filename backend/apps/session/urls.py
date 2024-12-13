from django.urls import path, include
from .views import exit, create_session, show_session, create_material, create_question, create_options, \
    show_questions, show_options, choose_num_options, answer_questions

urlpatterns = [
    path ('logout/', exit,name='exit'),
    path('create_session/<int:course_id>/', create_session, name='create_session'),
    path('create_material.html/', create_material, name='create_material.html'),
    path('create_question/', create_question, name='create_question'),
    path('create_options/', create_options, name='create_options'),
    path('s:<int:session_id>/', show_session, name='show_session'),
    path('create_session/', create_session, name='create_session'),
    path('s:<int:session_id>/create_material.html', create_material, name='create_material'),
    path('s:<int:session_id>/create_question', create_question, name='create_question'),
    path('s:<int:session_id>/q:<int:question_id>/n:<int:num_options>/create_options', create_options, name='create_options'),
    path('s:<int:session_id>/q:<int:question_id>/choose_num_options', choose_num_options, name='choose_num_options'),
    path('s:<int:session_id>/show_questions', show_questions, name='show_questions'),
    path('s:<int:session_id>/q:<int:question_id>/show_options', show_options, name='show_options'),
    path('s<int:session_id>/answer/', answer_questions, name='answer_questions'),
]
