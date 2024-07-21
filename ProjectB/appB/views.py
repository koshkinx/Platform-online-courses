from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

# Представление для списка и создания курсов
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()  # Получаем все объекты модели Course
    serializer_class = CourseSerializer  # Указываем сериализатор

# Представление для получения, обновления и удаления курса
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()  # Получаем все объекты модели Course
    serializer_class = CourseSerializer  # Указываем сериализатор
