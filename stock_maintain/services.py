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
    analysis = AnalysisOpinion.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )

    return analysis


def list_analysis_by_section(query_params):
    ''' List analysis for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')
    news = AnalysisOpinion.objects.filter(
        category_analysis__section_category__section_name__in=section_list
    )

    return news


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
    news = News.objects.filter(
        news_date__gte=s_date, news_date__lt=e_date
    )

    return news


def list_news_by_section(query_params):
    ''' List news   for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')
    news = News.objects.filter(
        category_news__section_category__section_name__in=section_list
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


def list_inside_business_by_section(query_params):
    ''' List inside business for a given date range'''

    try:
        section_list = query_params.get('section_list').split(',')
    except:
        raise APIException(detail='Provide section list')
    news = InsideBusiness.objects.filter(
        category_inside_business_section__section_category__section_name__in=section_list
    )

    return news


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
    articles = InsideBusiness.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )
    return articles