from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Item

class ItemAPITest(APITestCase):
    def test_create_item(self):
        url = reverse('item-list-create')
        data = {'name': 'Test Item', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Test Item')

    def test_get_items(self):
        Item.objects.create(name="Test Item", description="Test Description")
        url = reverse('item-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Item')

    def test_update_item(self):
        item = Item.objects.create(name="Test Item", description="Test Description")
        url = reverse('item-detail', args=[item.id])
        data = {'name': 'Updated Item', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, 'Updated Item')

    def test_delete_item(self):
        item = Item.objects.create(name="Test Item", description="Test Description")
        url = reverse('item-detail', args=[item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
