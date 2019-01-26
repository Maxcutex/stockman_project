import pdb
from datetime import datetime

import pytz
from rest_framework.exceptions import APIException

from stock_maintain.models import News, PriceList


def list_news_range(query_params):
	''' List news list for a given date range'''
	date_start = query_params.get('start_date').split('-')
	date_end = query_params.get('end_date').split('-')
	try:
		s_year = int(date_start[0])
		s_month = int(date_start[1])
		s_day = int(date_start[2])
		e_year = int(date_end[0])
		e_month = int(date_end[1])
		e_day = int(date_end[2])
		s_date = datetime(year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0).replace(tzinfo=pytz.UTC)
		e_date = datetime(year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0).replace(tzinfo=pytz.UTC)
	except:
		raise APIException(detail='Provide proper dates')
	news = News.objects.filter(
		news_date__gte=s_date,  news_date__lt=e_date
	)


	return news


def list_price_range(query_params):
	''' List prices for a given date range'''
	date_start = query_params.get('start_date').split('-')
	date_end = query_params.get('end_date').split('-')
	stock = int(query_params.get('stock'))
	try:
		s_year = int(date_start[0])
		s_month = int(date_start[1])
		s_day = int(date_start[2])
		e_year = int(date_end[0])
		e_month = int(date_end[1])
		e_day = int(date_end[2])
		s_date = datetime(year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0).replace(tzinfo=pytz.UTC)
		e_date = datetime(year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0).replace(tzinfo=pytz.UTC)
	except:
		raise APIException(detail='Provide proper dates')
	prices = PriceList.objects.filter(
		price_date__gte=s_date, price_date__lt=e_date, stock_id=stock
	)
	return prices