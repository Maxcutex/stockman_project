from __future__ import absolute_import, unicode_literals

import logging

from django.db import connection
import os
from datetime import datetime, date
from celery import Celery


from utils.utils import get_first_working_day_of_month

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockman_project.settings")
REDIS_URL = (os.environ.get("REDIS_URL", ""),)
app = Celery(
    "stockman_project",
    broker=f"{REDIS_URL}",
)
logger = logging.getLogger(__name__)
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


@app.task
def refresh_analysis_data(date_data):
    first_day_of_year = date(date.today().year, 1, 1)
    year_to_date = get_first_working_day_of_month(first_day_of_year)
    with connection.cursor() as cursor:
        return cursor.execute(
            f"call update_price_analysis('{date_data}','{year_to_date}')"
        )


@app.task
def process_csv_upload_task(date_import):
    print("entering transaction mode ....")
    logger.info("entering transaction mode ....")
    from stock_maintain.tasks import process_csv_upload

    process_csv_upload(date_import)
    refresh_analysis_data.delay(date_import)
    return True
