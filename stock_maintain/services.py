import pdb
from datetime import datetime

import django
import pytz
from django.db import connection
from rest_framework.exceptions import APIException

from stock_maintain.models import News, PriceList, AnalysisOpinion, InsideBusiness
from stock_setup_info.models import Stock, MainSector, SubSector, SectionGroup


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


def group_news_by_section():
    ''' group news for all the created sections'''

    section_list = SectionGroup.objects.all()

    news_list = []
    for section in section_list:
        list_news = News.objects.filter(
            category_news__section_category__section_name=section
        ).order_by("-id")[:5]
        for news in list_news:
            if len(news_list) == 0:
                news_list.append(news)
            else:
                found = False
                for news_list_item in news_list:
                    if news.id == news_list_item.id:
                        found = True
                if found == False:
                    news_list.append(news)

    return news_list


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


def search_list(sec_code, listDict):
    for p in listDict:
        if p['sec_code'] == sec_code:
            return p


def market_analysis(query_params):
    """ List prices and their corresponding percentage analysis by month ranges"""
    date_price = query_params.get('price_date')
    data_set = {}
    result_set = None
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute("BEGIN")
                cursor.callproc('get_price_market_analysis', [date_price])
                result_set = cursor.fetchall()
                cursor.execute("COMMIT")
                results = []
                count = 0
                for result in result_set:
                    dict_result = {}
                    count += 1
                    dict_result['id'] = count
                    dict_result['sec_code'] = result[0]
                    dict_result['price'] = result[1]
                    dict_result['min_year'] = result[2]
                    dict_result['max_year'] = result[3]
                    dict_result['min_six_months'] = result[4]
                    dict_result['max_six_months'] = result[5]
                    dict_result['min_three_months'] = result[6]
                    dict_result['max_three_months'] = result[7]
                    dict_result['min_one_week'] = result[8]
                    dict_result['max_one_week'] = result[9]
                    dict_result['price_one_week'] = result[10]
                    dict_result['price_three_months'] = result[11]
                    dict_result['price_six_months'] = result[12]
                    dict_result['price_one_year'] = result[13]
                    dict_result['one_week_cent'] = result[14]
                    dict_result['three_months_cent'] = result[15]
                    dict_result['six_months_cent'] = result[16]
                    dict_result['one_year_cent'] = result[17]

                    results.append(dict_result)
                result_by_main_sector = []

                for rs in results:
                    stock = Stock.objects.get(stock_code=rs['sec_code'])
                    final_sub_data = {}

                    if not any(d['main_sector'] == stock.sub_sector.main_sector.name for d in result_by_main_sector):
                        final_sub_data['main_sector'] = stock.sub_sector.main_sector.name
                        final_sub_data['sub_sector'] = stock.sub_sector.name
                        price_analysis = [rs]
                        final_sub_data['price_analysis'] = price_analysis
                        result_by_main_sector.append(final_sub_data)
                    else:
                        final_sub_data = [d for d in result_by_main_sector
                                          if d["main_sector"] == stock.sub_sector.main_sector.name][0]
                        final_sub_data['price_analysis'].append(rs)
                        result_by_main_sector_temp = [ d for d in result_by_main_sector
                                                       if d["main_sector"] != stock.sub_sector.main_sector.name]
                        result_by_main_sector_temp.append(final_sub_data)
                        result_by_main_sector = result_by_main_sector_temp

                data_set['results'] = result_by_main_sector
                data_set['count'] = count
            finally:
                cursor.close()
    except:
        raise APIException(detail='Provide proper date')

    return data_set


def list_price_date_by_sectors(query_params):
    """ List prices for a given date range by sectors"""

    price_date = query_params.get('price_date').split('-')
    try:
        price_year = int(price_date[0])
        price_month = int(price_date[1])
        price_day = int(price_date[2])

        s_date = datetime(year=price_year, month=price_month, day=price_day, hour=0, minute=0, second=0) \
            .replace(tzinfo=pytz.UTC)

    except:
        raise APIException(detail='Provide proper date')

    main_sector_list = MainSector.objects.all()
    date_sector_list = []
    id = 0
    for main_sector in main_sector_list:
        sub_sector_list = SubSector.objects.filter(main_sector_id=main_sector.id)

        for sub_sector in sub_sector_list:
            date_sector = {}
            stocks_involved = Stock.objects.filter(sub_sector_id=sub_sector.id).values_list('stock_code', flat=True)

            price_list_objects = PriceList.objects.filter(
                price_date=s_date, sec_code__in=stocks_involved)
            # pdb.set_trace()
            if price_list_objects:
                id += 1
                date_sector['id'] = id
                date_sector['sub_sector'] = sub_sector
                date_sector['sub_sector_name'] = sub_sector.name
                date_sector['main_sector_name'] = main_sector.name
                date_sector['main_sector'] = main_sector
                date_sector['price_list'] = price_list_objects

                date_sector_list.append(date_sector)

    return date_sector_list
