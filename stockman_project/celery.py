from __future__ import absolute_import, unicode_literals
from django.db import connection
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockman_project.settings")
REDIS_URL = (os.environ.get("REDIS_URL", ""),)
app = Celery(
    "stockman_project",
    broker=f"{REDIS_URL}",
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


@app.task
def refresh_analysis_data(date_data):
    with connection.cursor() as cursor:
        return cursor.callproc("update_price_analysis", date_data)
