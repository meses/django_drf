from rest_framework import serializers

from main.models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, object):
        return object.lessons.count()

    class Meta:
        model = Course
        fields = '__all__'
