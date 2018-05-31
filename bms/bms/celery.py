import os
from celery import Celery

if os.environ.get('CELERY_DEBUG'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bms.settingsdebug')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bms.settings')

app = Celery('bms')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
