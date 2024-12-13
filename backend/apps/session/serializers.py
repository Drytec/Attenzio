from rest_framework import serializers
from .models import Session, MaterialSession, Material, Question, Option


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id', 'session_name', 'session_description', 'session_date_start', 'session_date_end']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material_id', 'material_link']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'session_id']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option_id', 'option_text', 'is_correct', 'question_id']

