from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Course

class CourseAPITest(APITestCase):
    def test_create_course(self):
        url = reverse('course-list-create')
        data = {'title': 'Test Course', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().title, 'Test Course')

    def test_get_courses(self):
        Course.objects.create(title="Test Course", description="Test Description")
        url = reverse('course-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Course')

    def test_update_course(self):
        course = Course.objects.create(title="Test Course", description="Test Description")
        url = reverse('course-detail', args=[course.id])
        data = {'title': 'Updated Course', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course.refresh_from_db()
        self.assertEqual(course.title, 'Updated Course')

    def test_delete_course(self):
        course = Course.objects.create(title="Test Course", description="Test Description")
        url = reverse('course-detail', args=[course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)
