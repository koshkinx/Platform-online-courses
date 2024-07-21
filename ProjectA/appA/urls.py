from django.urls import path
from .views import ItemListCreate, ItemDetail

# URL маршруты для приложения appA
urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),  # Маршрут для списка и создания элементов
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),  # Маршрут для деталей элемента
]
