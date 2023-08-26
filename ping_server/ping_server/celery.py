import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ping_server.settings")

celery_app = Celery("ping_server_celery")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
