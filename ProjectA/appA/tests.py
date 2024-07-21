from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        # Создаем тестовый элемент
        Item.objects.create(name="Test Item", description="Test Description")

    def test_item_creation(self):
        # Проверяем, что элемент был создан корректно
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")
