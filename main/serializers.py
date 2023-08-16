from rest_framework import serializers

from main.models import Course, Lesson, Payments, CourseSubscription
from main.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_lessons_count(self, object):
        return object.lessons.count()

    def get_is_subscribed(self, obj):
        """Метод проверяет, авторизован ли текущий пользователь и подписан ли он на курс"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return CourseSubscription.objects.filter(user=request.user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

class CourseSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSubscription
        fields = '__all__'
