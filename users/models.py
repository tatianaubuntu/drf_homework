from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=15, verbose_name="имя")
    last_name = models.CharField(max_length=15, verbose_name="фамилия")
    phone = models.CharField(max_length=35, verbose_name="телефон")
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    country = models.CharField(max_length=35, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

