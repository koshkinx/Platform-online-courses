from django.db import models

# Модель для элементов (Items)
class Item(models.Model):
    name = models.CharField(max_length=100)  # Имя элемента
    description = models.TextField()  # Описание элемента

    def __str__(self):
        return self.name  # Возвращает строковое представление элемента
