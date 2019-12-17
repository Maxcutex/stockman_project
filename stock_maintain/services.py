import pdb
from datetime import datetime

import pytz
from rest_framework.exceptions import APIException

from stock_maintain.models import News, PriceList, AnalysisOpinion, InsideBusiness


def list_analysis_range(query_params):
    ''' List analysis for a given date range'''
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

    return AnalysisOpinion.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )


def list_analysis_by_section(query_params):
    ''' List analysis for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')
    return AnalysisOpinion.objects.filter(
        category_analysis__section_category__section_name__in=section_list
    )


def list_news_range(query_params):
    ''' List news   for a given date range'''
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
    return News.objects.filter(
        news_date__gte=s_date, news_date__lt=e_date
    )


def list_news_by_section(query_params):
    ''' List news   for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')
    return News.objects.filter(
        category_news__section_category__section_name__in=section_list
    )


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
    return PriceList.objects.filter(
        price_date__gte=s_date, price_date__lt=e_date, stock_id=stock
    )


def list_inside_business_by_section(query_params):
    ''' List inside business for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')

    return InsideBusiness.objects.filter(
        category_inside_business_section__section_category__section_name__in=section_list
    )


def list_inside_business_range(query_params):
    ''' List inside business  for a given date range'''
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
    return InsideBusiness.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )


def list_price_date(query_params):
    """ List prices for a given date range"""
    price_date = query_params.get('price_date').split('-')
    try:
        price_year = int(price_date[0])
        price_month = int(price_date[1])
        price_day = int(price_date[2])

        s_date = datetime(year=price_year, month=price_month, day=price_day, hour=0, minute=0, second=0) \
            .replace(tzinfo=pytz.UTC)

    except:
        raise APIException(detail='Provide proper date')
    return PriceList.objects.filter(
        price_date=s_date
    )
