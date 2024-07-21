from django.urls import path
from .views import CourseListCreate, CourseDetail

# URL маршруты для приложения appB
urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),  # Маршрут для списка и создания курсов
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),  # Маршрут для деталей курса
]
