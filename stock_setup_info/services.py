from rest_framework.exceptions import APIException
from django.db.models import Q
from stock_setup_info.models import Stock


def get_stock_by_code(query_params):
    ''' Get stock by the stock code provided'''

    try:
        stock_code = query_params.get('stock_code')
    except:
        raise APIException(detail='Provide proper stock code')
    return Stock.objects.filter(
        stock_code=stock_code
    )


def stock_search_like_name(query_params):
    ''' Get all stock with like search of name provided'''

    try:
        stock_code = query_params.get('stock_code')
    except:
        raise APIException(detail='Provide proper search variable')
    return Stock.objects.filter(Q(stock_code__contains=stock_code) | Q(name__contains=stock_code))
