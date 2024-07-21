from rest_framework import serializers
from .models import Course

# Сериализатор для модели Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course  # Указываем модель
        fields = '__all__'  # Включаем все поля модели
