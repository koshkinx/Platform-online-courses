from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# Представление для списка и создания элементов
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()  # Получаем все объекты модели Item
    serializer_class = ItemSerializer  # Указываем сериализатор

# Представление для получения, обновления и удаления элемента
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()  # Получаем все объекты модели Item
    serializer_class = ItemSerializer  # Указываем сериализатор
