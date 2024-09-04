from django.urls import path

from rest_framework.routers import DefaultRouter

from college.apps import CollegeConfig
from college.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionAPIView

app_name = CollegeConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='сourses')

urlpatterns = [

    #lesson
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    #subscription
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),

] + router.urls
