from django.db import models

# Модель для курсов (Courses)
class Course(models.Model):
    title = models.CharField(max_length=100)  # Название курса
    description = models.TextField()  # Описание курса

    def __str__(self):
        return self.title  # Возвращает строковое представление курса
