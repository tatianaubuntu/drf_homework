from django.core.management import BaseCommand

from college.models import Lesson, Course
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()

        users_list = [
            {
                'email': 'main@main.ru',
                'first_name': 'Николай',
                'last_name': 'Федотов',
                'phone': 89528953339,
                'country': 'Россия'
            }
        ]

        for user in users_list:
            User.objects.create(**user)

        Lesson.objects.all().delete()
        lessons_list = [
            {
                'title': 'Экономика',
                'description': 'Good',
            }
        ]
        for lesson in lessons_list:
            Lesson.objects.create(**lesson)

        Course.objects.all().delete()
        courses_list = [
            {
                'title': 'Высшая математика',
                'description': 'Good'
            }
        ]

        for course in courses_list:
            Course.objects.create(**course)

        Payment.objects.all().delete()
        payments_list = [
            {
                'date': '2011-04-28 18:00:00',
                'amount': 10000,
                'payment': 'cash',
                'user': User.objects.get(email='main@main.ru'),
                'lesson': Lesson.objects.get(title='Экономика')
            },
            {
                'date': '2011-10-24 10:00:00',
                'amount': 200000,
                'payment': 'remittance',
                'user': User.objects.get(email='main@main.ru'),
                'course': Course.objects.get(title='Высшая математика')
            }
        ]
        payments_for_create = []

        for payment in payments_list:
            payments_for_create.append(Payment(**payment))

        Payment.objects.bulk_create(payments_for_create)
