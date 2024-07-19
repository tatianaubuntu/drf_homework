from django.contrib.auth.models import AbstractUser
from django.db import models

from college.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,
                              verbose_name='почта')
    first_name = models.CharField(max_length=15,
                                  verbose_name="имя")
    last_name = models.CharField(max_length=15,
                                 verbose_name="фамилия")
    phone = models.CharField(max_length=35,
                             verbose_name="телефон")
    avatar = models.ImageField(upload_to='users/',
                               verbose_name='аватар',
                               **NULLABLE)
    country = models.CharField(max_length=35,
                               verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    payment_tuple = (
        ('cash', 'наличные'),
        ('remittance', 'перевод на счет'),
    )
    date = models.DateTimeField(verbose_name='дата и время оплаты')
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment = models.CharField(max_length=150,
                               verbose_name='способ оплаты',
                               choices=payment_tuple)

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             verbose_name='пользователь',
                             **NULLABLE)
    course = models.ForeignKey('college.Course',
                               on_delete=models.SET_NULL,
                               **NULLABLE,
                               verbose_name='оплаченный курс')
    lesson = models.ForeignKey('college.Lesson',
                               on_delete=models.SET_NULL,
                               **NULLABLE,
                               verbose_name='оплаченный урок')

    def __str__(self):
        return f'{self.user} - {self.amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-payment',)
