# Платформа для онлайн-курсов

## Описание

Этот проект представляет собой платформу для онлайн-курсов с функциональностью проведения тестирования, автоматической оценки результатов, проведения вебинаров и видеоуроков в режиме реального времени, а также индивидуальных консультаций для студентов.

Проект состоит из двух отдельных Django проектов: "ProjectA" и "ProjectB".

## Функциональность

1. **Розробка двох Django проектів**: Створення двох окремих Django проектів - "ProjectA" та "ProjectB".
2. **REST API**: Реалізація REST API для створення, оновлення, видалення та отримання даних.
3. **Комунікація через API**: Налаштування взаємодії між "ProjectA" та "ProjectB" через їхні REST API.
4. **Docker**: Контейнеризація кожного Django проекту з використанням Docker.
5. **Тести**: Написання модульних, функціональних та інтеграційних тестів.
6. **Таски**: Використання Celery для асинхронного виконання завдань.
7. **Class Based Views та наслідування**: Використання Class Based Views для створення сторінок та функціональності.
8. **Перевизначення моделі користувача та пермішини**: Розширення вбудованої моделі користувача або створення власної моделі користувача.
9. **Bootstrap**: Використання фреймворку Bootstrap для створення стилізованого та адаптивного інтерфейсу.

## Установка

### Системные требования

- Python 3.12
- Docker
- Docker Compose

### Настройка проекта

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/koshkinx/your-repo.git
    cd your-repo
    ```

2. Создайте и активируйте виртуальное окружение:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # для Windows
    source .venv/bin/activate  # для MacOS/Linux
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:
    ```sh
    python manage.py migrate
    ```

### Запуск проекта

1. Запустите Docker Compose:
    ```sh
    docker-compose up --build
    ```

2. Выполните миграции базы данных для контейнера `projecta`:
    ```sh
    docker-compose exec projecta python manage.py migrate
    ```

3. Запустите Celery worker:
    ```sh
    docker-compose exec projecta celery -A ProjectA worker --loglevel=info
    ```

### Тестирование

1. Запустите тесты для `ProjectA`:
    ```sh
    docker-compose exec projecta python manage.py test
    ```

2. Запустите тесты для `ProjectB`:
    ```sh
    docker-compose exec projectb python manage.py test
    ```

## Контрибьюция

Если вы хотите внести вклад в проект, пожалуйста, создайте pull request.

## Лицензия

Этот проект лицензирован под MIT License.
