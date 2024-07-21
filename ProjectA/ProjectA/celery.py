from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectA.settings')

app = Celery('ProjectA')

# Используем настройки Django в Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в ваших приложениях
app.autodiscover_tasks()
