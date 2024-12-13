from rest_framework import serializers
from .models import Course, CustomUserCourse

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_schedule']

class CustomUserCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = CustomUserCourse
        fields = ['custom_user_course_id', 'custom_user_id', 'course_id']