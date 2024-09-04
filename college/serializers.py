from rest_framework import serializers

from college.models import Course, Lesson
from college.validators import UrlValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    link_to_video = serializers.URLField(validators=[UrlValidator()])

    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriptionUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)
    subscription = SubscriptionUserSerializer(source='subscription_set.all.user',
                                          many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson.all().count()


