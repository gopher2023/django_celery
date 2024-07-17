import os
from celery import Celery

app = Celery('mycelery')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycelery.settings')
app.config_from_object('mycelery.config')
app.autodiscover_tasks(['mycelery.books'])