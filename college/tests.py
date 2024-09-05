from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from college.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.ru')
        self.course = Course.objects.create(
            title='test',
            description='test'
        )
        self.lesson = Lesson.objects.create(
            title='test',
            description='test',
            course=self.course,
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_lesson(self):
        """ Тестирование вывода одного урока """
        url = reverse('college:lesson-detail', args=[self.lesson.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_create_lesson(self):
        """ Тестирование создания урока """
        url = reverse('college:lesson-create')
        data = {
            'title': 'new test',
            'description': 'new test',
            'link_to_video': 'https://youtube.com/lesson',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, Lesson.objects.all().count())

    def test_update_lesson(self):
        """ Тестирование редактирования урока """
        url = reverse('college:lesson-update', args=[self.lesson.pk])
        data = {
            'title': 'update test'
        }
        response = self.client.patch(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), 'update test')

    def test_destroy_lesson(self):
        """ Тестирование удаления урока """
        url = reverse('college:lesson-delete', args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Lesson.objects.all().count())

    def test_list_lesson(self, null=None):
        """ Тестирование вывода списка уроков """
        url = reverse('college:lesson-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link_to_video": self.lesson.link_to_video,
                    "title": self.lesson.title,
                    "preview": null,
                    "description": self.lesson.description,
                    "course": self.lesson.course.pk,
                    "owner": self.lesson.owner.pk
                }
            ]
        }
        data = response.json()
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.ru')

        self.course_1 = Course.objects.create(
            title='test',
            description='test',
            owner=self.user

        )
        self.course_2 = Course.objects.create(
            title='test2',
            description='test2',
            owner=self.user

        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course_1
        )
        self.client.force_authenticate(user=self.user)

    def test_post_subscription(self):
        """ Тестирование подписки на курс """
        url = reverse('college:subscription')
        data_1 = {
            'user': self.user.pk,
            'course': self.course_1.pk
        }
        data_2 = {
            'user': self.user.pk,
            'course': self.course_2.pk
        }

        response_1 = self.client.post(url, data_1)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(0, Subscription.objects.all().count())
        response_2 = self.client.post(url, data_2)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(1, Subscription.objects.all().count())