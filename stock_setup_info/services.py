from rest_framework.exceptions import APIException
from django.db.models import Q

from stock_maintain.models import PriceList
from stock_setup_info.models import Stock


def get_stock_by_code(query_params):
    """ Get stock by the stock code provided"""

    try:
        stock_code = query_params.get("stock_code")
    except Exception:
        raise APIException(detail="Provide proper stock code")
    return Stock.objects.filter(stock_code=stock_code)[:1][0]


def stock_search_like_name(query_params):
    """ Get all stock with like search of name provided"""

    try:
        stock_code = query_params.get("stock_code")
    except Exception:
        raise APIException(detail="Provide proper search variable")
    return Stock.objects.filter(
        Q(stock_code__contains=stock_code) | Q(name__contains=stock_code)
    )


def stock_competitors(query_params):
    """
    Return list of all competitors to current stock

    :param query_params: query parameters on the url
    :return: list of all competitiors stock
    """

    try:
        stock_code = query_params.get("stock_code")
        if stock_code is None or stock_code == "":
            raise APIException(detail="Provide stock code for search")
    except Exception:
        raise APIException(detail="Provide stock code for search")
    stock = Stock.objects.filter(stock_code=stock_code)[:1][0]

    stocks = Stock.objects.filter(
        ~Q(stock_code=stock_code) & Q(industry=stock.industry)
    )
    competitors = []
    for stock_record in stocks:
        price_data = PriceList.objects.filter(
            sec_code=stock_record.stock_code
        ).order_by("-price_date")[:1][0]
        stock_details = {
            "stock_code": stock_record.stock_code,
            "price": price_data.price,
            "change_data": str(price_data.offer_bid_sign)
            + str(f"{price_data.x_change:.2f}")
            + "%",
            "market_data": price_data.volume,
        }
        competitors.append(stock_details)
    return competitors
