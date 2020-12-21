# Create your tasks here
from __future__ import absolute_import, unicode_literals

import csv
import io
import logging
import os
from datetime import datetime

from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail
from celery import shared_task
from django.db import connection
from django.shortcuts import redirect
from psycopg2._psycopg import IntegrityError
from stockman_project.celery import refresh_analysis_data

from stock_maintain.models import PriceList, GeneratedAnalysisDate
from stock_setup_info.models import Stock

logger = logging.getLogger(__name__)


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


@shared_task
def process_csv_upload(date_import):
    # download_location = f"/tmp/{date_import}.csv"
    error_found = ""

    import boto3

    s3 = boto3.resource("s3")
    # s3.meta.client.download_file("csv_uploads", f"{date_import}.csv", download_location)
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    PUBLIC_CSV_LOCATION = "csv_uploads"
    file_name = f"{date_import}.csv"
    object_name = "{}/{}".format(PUBLIC_CSV_LOCATION, file_name)
    result = s3.meta.client.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=object_name)
    # content = result["Body"].read()
    decoded_csv_file = io.StringIO(result["Body"].read().decode("utf-8"))
    reader = csv.reader(decoded_csv_file)
    new_date = datetime.strptime(date_import, "%Y-%m-%d")
    print(f"PRINT: finished reading file....for date {new_date}")
    logger.info(f"LOG: importing file....for date {new_date}")
    # Create pricelist objects from passed in data
    try:
        print("entering transaction mode ...")
        logger.info("entering transaction mode ....")
        # with transaction.atomic():
        print("PRINT: starting each data")
        logger.info("LOG: starting each data")

        for line in reader:
            # pdb.set_trace()

            stock_code = line[0].strip()

            print(f"PRINT: getting current stock - {stock_code}")
            logger.info(f"LOG: getting current stock - {stock_code}")
            uploaded_stock = PriceList.objects.filter(
                sec_code=stock_code, price_date=new_date
            )
            if uploaded_stock:
                stock = Stock.objects.get(stock_code=stock_code)

                # pdb.set_trace()
                if stock:
                    x_change = 0.0
                    sign = ""
                    if line[1].strip() == "" or line[6].strip() == "":
                        # pdb.set_trace()
                        error_found = (
                            f"The stock {stock_code} has no data in the pricelist. "
                            f"Kindly review your csv and upload correct data"
                        )
                        raise ValueError()
                    if float(line[1].strip()) <= float(line[6].strip()):
                        sign = "+"
                        x_change = float(line[6]) - float(line[1])
                    else:
                        sign = "-"
                        x_change = float(line[1]) - float(line[6])
                    # pdb.set_trace()
                    price_list_object = PriceList.objects.create(
                        sec_code=line[0],
                        price_date=new_date,  # line[12],
                        price_close=float(line[6].strip()),
                        x_open=float(line[2].strip()),
                        x_high=float(line[3].strip()),
                        x_low=float(line[4].strip()),
                        price=float(line[1].strip()),
                        offer_bid_sign=sign,
                        x_change=x_change,
                        num_of_deals=float(line[9].strip().replace(",", "")),
                        volume=float(line[10].strip().replace(",", "")),
                        x_value=float(line[11].strip().replace(",", "")),
                        stock_id=stock.id,
                    )
                    # pdb.set_trace()
                    print(f"PRINT: attempting to save current stock pric- {stock_code}")
                    logger.info(f"LOG: attempting current stock price- {stock_code}")
                    price_list_object.save()
                else:
                    error_found = f"The stock {stock_code} could not be found"
                    # pdb.set_trace()
                    raise ValueError()
            else:
                continue
        print("finished importing")
        logger.info(" finishedimporting file ....")
        # trigger a cron job re-calculate temp table
        print("about to send delay task")
        logger.info("about to send delay task ....")
        refresh_analysis_data.delay(date_import)

    except ValueError:
        if error_found == "":
            error_found = (
                f"The stock {line[0].strip()} had error in its values. Pls check"
            )
        logger.info(error_found)
    except Stock.DoesNotExist:
        logger.error(
            "Stock Not Exist: A stock value does not exist in the database ...."
        )

    except IntegrityError:
        logger.error(
            "Data Integritiy Error: A stock value does not exist in the database. ...."
        )
