from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Course, Lesson, CourseSubscription
from users.models import User


class mainTestCase(APITestCase):

    def setUp(self):

        # Создание тестового пользователя
        self.user = User.objects.create_user(
            email='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

        # Создание тестового курса
        self.course = Course.objects.create(
            title='Тестовый курс',
            description='Описание тестового курса',
            owner=self.user
        )
        print(self.course.pk)

    def test_create_lesson(self):
        """ Тестирование создания урока """
        data = {
            'title': 'Test',
            'description': 'Test',
            'course': self.course.id
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        # Тест, что объект создался
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Тест, что созданный объект соответствует ожиданиям
        self.assertEqual(
            response.json(),
            {'id': 1, 'video_link': None, 'title': 'Test', 'preview': None, 'description': 'Test', 'course': 2,
             'owner': 2}
        )

        # Тест, что объект записан в БД
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_update_lesson(self):
        """Тестирование обновления урока"""

        lesson = Lesson.objects.create(
            title='Test',
            description='Test',
            video_link='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )

        data = {
            'title': 'Test_new',
            'description': 'Test_new',
            'video_link': 'https://www.youtube.com/',
            'course': self.course.pk
        }

        url = reverse('main:lesson_update', kwargs={'pk': lesson.pk})
        response = self.client.put(url, data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['title'], data['title'])
        self.assertEquals(response.data['description'], data['description'])


    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        lesson = Lesson.objects.create(
            title='Test',
            description='Test',
            video_link='https://www.youtube.com/',
            course=self.course,
            owner=self.user
            )
        url = reverse('main:lesson_delete', kwargs={'pk': lesson.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=lesson.id).exists())


    def test_create_course_subscription(self):
        """Тестирование создания подписки"""

        url = reverse('main:coursesubscription_create')
        data = {
            'course': self.course.id,
            'user': self.user.id,
            'is_subscribed': True
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        subscription = CourseSubscription.objects.get(user=self.user, course=self.course)
        self.assertTrue(subscription.is_subscribed)

    def test_delete_course_subscription(self):
        """Тестирование удаления подписки"""

        subscription = CourseSubscription.objects.create(user=self.user, course=self.course, is_subscribed=True)
        url = reverse('main:coursesubscription_delete', kwargs={'pk': subscription.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CourseSubscription.objects.filter(id=subscription.id).exists())
