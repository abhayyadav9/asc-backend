from rest_framework import serializers
from .models import Course, Instance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class InstanceSerializer(serializers.ModelSerializer):
    course_details = CourseSerializer(source='course', read_only=True)  # For reading course details
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())  # For writing course ID

    class Meta:
        model = Instance
        fields = ['id', 'year', 'semester', 'course', 'course_details'] 