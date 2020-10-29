from datetime import datetime, timedelta
from django.db.models import Max, Min
import pytz
from django.conf.global_settings import DATE_FORMAT
from django.db import connection
from rest_framework.exceptions import APIException

from stock_maintain.models import (
    News,
    PriceList,
    AnalysisOpinion,
    InsideBusiness,
    NewsLetterMailing,
    PriceAnalysisTemp,
)
from stock_maintain.serializers import PriceListSerializer
from stock_setup_info.models import Stock, MainSector, SubSector, SectionGroup


def list_analysis_range(query_params):
    """ List analysis for a given date range"""
    date_start = query_params.get("start_date").split("-")
    date_end = query_params.get("end_date").split("-")
    try:
        s_year = int(date_start[0])
        s_month = int(date_start[1])
        s_day = int(date_start[2])
        e_year = int(date_end[0])
        e_month = int(date_end[1])
        e_day = int(date_end[2])
        s_date = datetime(
            year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
        e_date = datetime(
            year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
    except Exception:
        raise APIException(detail="Provide proper dates")

    return AnalysisOpinion.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )


def list_analysis_by_section(query_params):
    """ List analysis for a given date range"""

    try:
        section_list = query_params.get("section_list").split(",")
    except Exception:
        raise APIException(detail="Provide section list")
    return AnalysisOpinion.objects.filter(
        category_analysis__section_category__section_name__in=section_list
    )


def list_newsletterusers_by_active():
    """ List active users of newsletter"""

    return NewsLetterMailing.objects.filter(is_active=True)


def list_news_range(query_params):
    """
    List news   for a given date range
    """
    date_start = query_params.get("start_date").split("-")
    date_end = query_params.get("end_date").split("-")
    try:
        s_year = int(date_start[0])
        s_month = int(date_start[1])
        s_day = int(date_start[2])
        e_year = int(date_end[0])
        e_month = int(date_end[1])
        e_day = int(date_end[2])
        s_date = datetime(
            year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
        e_date = datetime(
            year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
    except Exception:
        raise APIException(detail="Provide proper dates")
    return News.objects.filter(news_date__gte=s_date, news_date__lt=e_date)


def list_news_by_section(query_params):
    """ List news   for a given date range"""

    try:
        section_list = query_params.get("section_list").split(",")
    except Exception:
        raise APIException(detail="Provide section list")
    return News.objects.filter(
        category_news__section_category__section_name__in=section_list
    )


def group_news_by_section():
    """ group news for all the created sections"""

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
                if not found:
                    news_list.append(news)

    return news_list


def list_price_range(query_params):
    """ List prices for a given date range"""
    date_start = query_params.get("start_date").split("-")
    date_end = query_params.get("end_date").split("-")
    stock = int(query_params.get("stock"))
    try:
        s_year = int(date_start[0])
        s_month = int(date_start[1])
        s_day = int(date_start[2])
        e_year = int(date_end[0])
        e_month = int(date_end[1])
        e_day = int(date_end[2])
        s_date = datetime(
            year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
        # s_date = datetime(year=2019, month=1, day=22, hour=0, minute=0, second=0)
        e_date = datetime(
            year=e_year,
            month=e_month,
            day=e_day,
            hour=0,
            minute=0,
            second=0,
            tzinfo=pytz.UTC,
        ).replace(tzinfo=pytz.UTC)

    except Exception:
        raise APIException(detail="Provide proper dates")
    return PriceList.objects.filter(
        price_date__gte=s_date, price_date__lt=e_date, stock_id=stock
    )


def list_inside_business_by_section(query_params):
    """ List inside business for a given date range"""

    try:
        section_list = query_params.get("section_list").split(",")

    except Exception:
        raise APIException(detail="Provide section list")

    return InsideBusiness.objects.filter(
        category_inside_business_section__section_category__section_name__in=section_list
    )


def list_inside_business_range(query_params):
    """ List inside business  for a given date range"""
    date_start = query_params.get("start_date").split("-")
    date_end = query_params.get("end_date").split("-")
    try:
        s_year = int(date_start[0])
        s_month = int(date_start[1])
        s_day = int(date_start[2])
        e_year = int(date_end[0])
        e_month = int(date_end[1])
        e_day = int(date_end[2])
        s_date = datetime(
            year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
        e_date = datetime(
            year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0
        ).replace(tzinfo=pytz.UTC)
    except Exception:
        raise APIException(detail="Provide proper dates")
    return InsideBusiness.objects.filter(
        opinion_date__gte=s_date, opinion_date__lt=e_date
    )


def list_price_date(query_params):
    """ List prices for a given date range"""

    price_date = split_date(query_params.get("price_date"))

    try:
        price_year = int(price_date[0])
        price_month = int(price_date[1])
        price_day = int(price_date[2])

        s_date = datetime(
            year=price_year,
            month=price_month,
            day=price_day,
            hour=0,
            minute=0,
            second=0,
        ).replace(tzinfo=pytz.UTC)

    except Exception:
        raise APIException(detail="Provide proper date")

    return PriceList.objects.filter(price_date=s_date)


def search_list(sec_code, listDict):
    for p in listDict:
        if p["sec_code"] == sec_code:
            return p


def market_analysis_stock(query_params):
    """
    List prices and their corresponding percentage analysis by stock
    """
    dict_result = {}
    try:
        sec_code = query_params.get("sec_code")
        if sec_code is not None:
            rs = PriceAnalysisTemp.objects.filter(sec_code=sec_code).first()
            price_data = PriceList.objects.filter(sec_code=sec_code).order_by(
                "-price_date"
            )[:1][0]

            if rs:

                f52_week_monday = price_data.price_date - timedelta(
                    days=price_data.price_date.weekday(), weeks=-52
                )
                f52_week_friday = (
                    price_data.price_date
                    - timedelta(days=price_data.price_date.weekday())
                    + timedelta(days=4, weeks=-52)
                )
                price_group = PriceList.objects.filter(
                    sec_code=sec_code,
                    price_date__gte=f52_week_monday,
                    price_date__lte=f52_week_friday,
                )
                max_52_week = price_group.aggregate(Max("price"))
                min_52_week = price_group.aggregate(Min("price"))
                dict_result = {
                    "id": rs.id,
                    "sec_code": rs.sec_code,
                    "price": rs.price,
                    "min_year": rs.min_year,
                    "max_year": rs.max_year,
                    "min_six_months": rs.min_six_months,
                    "max_six_months": rs.max_six_months,
                    "min_three_months": rs.min_three_months,
                    "max_three_months": rs.max_three_months,
                    "min_one_week": rs.min_one_week,
                    "max_one_week": rs.max_one_week,
                    "price_one_week": rs.price_one_week,
                    "price_three_months": rs.price_three_months,
                    "price_six_months": rs.price_six_months,
                    "price_one_year": rs.price_one_year,
                    "one_week_cent": rs.one_week_cent,
                    "three_months_cent": rs.three_months_cent,
                    "six_months_cent": rs.six_months_cent,
                    "one_year_cent": rs.one_year_cent,
                    "price_year_to_date_cent": rs.price_year_to_date_cent,
                    "previous_price": price_data.price,
                    "current_price": price_data.price_close,
                    "today_change": float(f"{price_data.x_change:.2f}"),
                    "today_sign": price_data.offer_bid_sign,
                    "today_volume": price_data.volume,
                    "today_day_range": f"{price_data.x_low} - {price_data.x_high}",
                    "today_52_week_range": f"{min_52_week} - {max_52_week}",
                }

        # data_set['results'] = dict_result
        # data_set['date'] = date_price

    except Exception:
        raise APIException(detail="Provide proper date or sec code")

    return dict_result


def market_analysis(query_params):
    """ List prices and their corresponding percentage analysis by month ranges"""

    try:
        date_price = query_params.get("price_date")
        if date_price is None:
            last_date = PriceList.objects.order_by("-price_date")[:1][0]
            date_price = str(last_date.price_date)

        price_analysis = PriceAnalysisTemp.objects.filter(price_date__date=date_price)
        data_set = {}
        count = 0
        result_by_main_sector = []
        for rs in price_analysis:
            dict_result = {}
            count += 1
            dict_result["id"] = count
            dict_result["sec_code"] = rs.sec_code
            dict_result["price"] = rs.price
            dict_result["min_year"] = rs.min_year
            dict_result["max_year"] = rs.max_year
            dict_result["min_six_months"] = rs.min_six_months
            dict_result["max_six_months"] = rs.max_six_months
            dict_result["min_three_months"] = rs.min_three_months
            dict_result["max_three_months"] = rs.max_three_months
            dict_result["min_one_week"] = rs.min_one_week
            dict_result["max_one_week"] = rs.max_one_week
            dict_result["price_one_week"] = rs.price_one_week
            dict_result["price_three_months"] = rs.price_three_months
            dict_result["price_six_months"] = rs.price_six_months
            dict_result["price_one_year"] = rs.price_one_year
            dict_result["one_week_cent"] = rs.one_week_cent
            dict_result["three_months_cent"] = rs.three_months_cent
            dict_result["six_months_cent"] = rs.six_months_cent
            dict_result["one_year_cent"] = rs.one_year_cent

            final_sub_data = {}

            if not any(
                d["main_sector"] == rs.stock.sub_sector.main_sector.name
                for d in result_by_main_sector
            ):
                final_sub_data["main_sector"] = rs.stock.sub_sector.main_sector.name
                final_sub_data["sub_sector"] = rs.stock.sub_sector.name
                price_analysis = [dict_result]
                final_sub_data["price_analysis"] = price_analysis
                result_by_main_sector.append(final_sub_data)
            else:
                final_sub_data = [
                    d
                    for d in result_by_main_sector
                    if d["main_sector"] == rs.stock.sub_sector.main_sector.name
                ][0]
                final_sub_data["price_analysis"].append(dict_result)
                result_by_main_sector_temp = [
                    d
                    for d in result_by_main_sector
                    if d["main_sector"] != rs.stock.sub_sector.main_sector.name
                ]
                result_by_main_sector_temp.append(final_sub_data)
                result_by_main_sector = result_by_main_sector_temp
        sorted_result = sorted(result_by_main_sector, key=lambda k: k["main_sector"])
        data_set["results"] = sorted_result
        data_set["date"] = date_price
        data_set["count"] = count

    except Exception:
        raise APIException(detail="Provide proper date")

    return data_set


def split_date(date_to_split):
    return date_to_split.split("-")


def list_price_date_by_sectors(query_params):
    """ List prices for a given date range by sectors"""

    price_date = split_date(query_params.get("price_date"))

    try:
        price_year = int(price_date[0])
        price_month = int(price_date[1])
        price_day = int(price_date[2])

        s_date = datetime(
            year=price_year,
            month=price_month,
            day=price_day,
            hour=0,
            minute=0,
            second=0,
        ).replace(tzinfo=pytz.UTC)

    except Exception:
        raise APIException(detail="Provide proper date")

    main_sector_list = MainSector.objects.all()
    date_sector_list = []
    id = 0
    for main_sector in main_sector_list:
        sub_sector_list = SubSector.objects.filter(main_sector_id=main_sector.id)

        for sub_sector in sub_sector_list:
            date_sector = {}
            stocks_involved = Stock.objects.filter(
                sub_sector_id=sub_sector.id
            ).values_list("stock_code", flat=True)

            price_list_objects = PriceList.objects.filter(
                price_date=s_date, sec_code__in=stocks_involved
            )
            # pdb.set_trace()
            if price_list_objects:
                price_list_objects.order_by("sec_code")
                id += 1
                date_sector["id"] = id
                date_sector["sub_sector"] = sub_sector
                date_sector["sub_sector_name"] = sub_sector.name
                date_sector["main_sector_name"] = main_sector.name
                date_sector["main_sector"] = main_sector
                date_sector["price_list"] = price_list_objects

                date_sector_list.append(date_sector)

    return date_sector_list
