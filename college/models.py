from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='название')
    preview = models.ImageField(upload_to='college/',
                                verbose_name='картинка',
                                **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='название')
    preview = models.ImageField(upload_to='college/',
                                verbose_name='картинка',
                                **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link_to_video = models.URLField(verbose_name='ссылка на видео',
                                    **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               verbose_name='курс',
                               **NULLABLE,
                               related_name='lesson')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
