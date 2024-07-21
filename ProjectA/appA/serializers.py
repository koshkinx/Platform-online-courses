from rest_framework import serializers
from .models import Item

# Сериализатор для модели Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item  # Указываем модель
        fields = '__all__'  # Включаем все поля модели
