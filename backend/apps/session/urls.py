from django.urls import path
from .views import ShowSessionView, CreateSessionView, CreateMaterialView, CreateQuestionView, CreateOptionsView


urlpatterns = [
    path('logout/', exit, name='exit'),
    path('api/sessions/', CreateSessionView.as_view(), name='create_session'),
    path('api/sessions/<int:session_id>/', ShowSessionView.as_view(), name='show_session'),
    path('api/sessions/<int:session_id>/materials/', CreateMaterialView.as_view(), name='create_material'),
    path('api/sessions/<int:session_id>/questions/', CreateQuestionView.as_view(), name='create_question'),
    path('api/sessions/<int:session_id>/questions/<int:question_id>/options/', CreateOptionsView.as_view(), name='create_options'),
]

