from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', exit, name='exit'),
    path('create_session/', CreateSessionView.as_view(), name='create_session'),
    path('s:<int:session_id>/', ShowSessionView.as_view(), name='show_session'),
    path('s:<int:session_id>/create_material', CreateMaterialView.as_view(), name='create_material'),
    path('s:<int:session_id>/create_question', CreateQuestionView.as_view(), name='create_question'),
    path('s:<int:session_id>/q:<int:question_id>/create_options', CreateOptionsView.as_view(), name='create_options'),
    path('s:<int:session_id>/show_questions', ShowQuestionsView.as_view(), name='show_questions'),
    path('s:<int:session_id>/q:<int:question_id>/show_options', ShowOptionsView, name='show_options'),
]

