from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        # Создаем тестовый курс
        Course.objects.create(title="Test Course", description="Test Description")

    def test_course_creation(self):
        # Проверяем, что курс был создан корректно
        course = Course.objects.get(title="Test Course")
        self.assertEqual(course.description, "Test Description")
