# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail
from celery import shared_task
from django.db import connection

from stock_maintain.models import PriceList, GeneratedAnalysisDate


@shared_task
def send_mail_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
    return None


@periodic_task(
    run_every=(crontab(hour=21, minute=10, day_of_week="mon-fri")),
    name="update_price_analysis",
    ignore_result=True,
)
def update_price_analysis_task():
    # get last date
    last_date = PriceList.objects.order_by("-price_date")[:1][0]

    # check if last date has been processed in processed table
    generated_report = GeneratedAnalysisDate.objects.get(date_price=last_date)
    if generated_report is None:
        with connection.cursor() as cursor:
            try:
                # pdb.set_trace()
                cursor.execute(f"CALL process_price_market_analysis('{last_date}')")

            finally:
                cursor.close()
