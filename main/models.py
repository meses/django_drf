from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    video_link = models.CharField(max_length=255, verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey('Course', default=1, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Payments(models.Model):

    choices_payment_method = [
        ('cash', 'Наличные'),
        ('transfer to account', 'Перевод на счет')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    payment_date = models.DateTimeField(default=timezone.now, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='paid_course',
                                    verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='paid_lesson',
                                    verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=choices_payment_method, verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.user}, {self.paid_course or self.paid_lesson}, {self.payment_method}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
