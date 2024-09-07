from rest_framework import serializers

from college.models import Course, Lesson, Subscription
from college.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    link_to_video = serializers.URLField(validators=[UrlValidator()])

    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Subscription
        fields = ['user_email']


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)
    subscription = SubscriptionSerializer(source='subscription_set',
                                          many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson.all().count()


