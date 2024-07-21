# Используем официальный Python образ в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8001 для доступа к приложению
EXPOSE 8001

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
