from rest_framework import status
from rest_framework.test import APITestCase

from .models import Student
from users.models import User


class StudentsTestCase(APITestCase):
    """Тест энпоинтов студента"""

    def setUp(self) -> None:
        """Создание тестовых данных"""

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="1255753717",
            roles=("moderator", "teacher", "student")
        )

        self.data = Student.objects.create(
                first_name="Ivan",
                last_name="Ivanov",
        )

        self.client.force_authenticate(user=self.user)

    def test_1_create_student(self):
        """ Тестирование создания студента """

        data = {
            "first_name": "Ivan",
            "last_name": "Ivanov",
        }

        response = self.client.post('/students/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.all().count(), 2)

    def test_2_list_student(self):
        """ Тестирование вывода списка студентов """

        response = self.client.get('/students/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.all().count(), 1)

    def test_3_list_all_students(self):
        """ Тестирование вывода полных данных списка студентов """

        response = self.client.get('/students/all/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.all().count(), 1)

    def test_4_update_students(self):
        """ Тестирование обновления данных о студентах """

        data = {
                "first_name": "Ivan",
                "last_name": "Ivanov",
        }

        response = self.client.put(f'/students/update/{self.data.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], 'Ivan')

    def test_5_destroy_students(self):
        """ Тестирование удаления студента """

        response = self.client.delete(f'/students/delete/{self.data.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.all().exists())
        self.assertEqual(Student.objects.all().count(), 0)
        