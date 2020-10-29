from rest_framework.exceptions import APIException
from django.db.models import Q

from stock_maintain.models import PriceList, QuarterlyFinancial, DividendInformation
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


def stock_statistics(query_params):
    """
    Return list of a stock's statistics

    :param query_params: query parameters on the url
    :return: list of all statistics
    """
    try:
        stock_code = query_params.get("stock_code")
        if stock_code is None or stock_code == "":
            raise APIException(detail="Provide stock code for search")
    except Exception:
        raise APIException(detail="Provide stock code for search")
    stock = Stock.objects.filter(stock_code=stock_code)[:1][0]
    stock_in_market = PriceList.objects.filter(sec_code=stock_code).order_by(
        "-price_date"
    )[:1][0]
    stock_analytics_info = QuarterlyFinancial.objects.filter(sec_code=stock_code)[:1][0]
    stock_dividend_info = DividendInformation.objects.filter(
        sec_code=stock_code
    ).order_by("-year", "-period_number")[:1]
    valuation = {
        "probability": {
            "pat_margin": 0.0,
            "roe": 0.0,
            "dps": 0.0,
            "period": 0,
        },
        "valuation": {
            "pe_ratio": 0.0,
            "net_asset_per_share": 0.0,
            "eps": 0.0,
            "dividend_yield": 0.0,
        },
        "company_statistics": {
            "registrars": "",
            "listing_date": "",
            "year_end": "",
            "share_outstanding": stock.outstanding_shares,
        },
        "kpi": {
            "turnover_growth": 0.0,
            "pat_growth": 0.0,
            "net_assets_growth": 0.0,
            "assets_growth": 0.0,
        },
    }
    if stock_analytics_info and stock_dividend_info:
        pat_margin = round(
            (stock_analytics_info.profit_after_tax / stock_analytics_info.turnover)
            * 100,
            2,
        )
        roe = round(
            (stock_analytics_info.profit_after_tax / stock_analytics_info.net_assets)
            * 100,
            2,
        )

        switcher = {
            1: "1st Quarter",
            2: "2nd Quarter",
            3: "3rd Quarter",
            4: "4th Quarter",
        }

        period = switcher.get(stock_analytics_info.period_number, "Invalid Quarter")
        valuation["probability"] = {
            "pat_margin": pat_margin,
            "roe": roe,
            "dps": stock_dividend_info.dividend_value,
            "period": period,
        }
        eps = round(stock_analytics_info.profit_after_tax / stock.outstanding_shares, 2)
        naps = round(stock_analytics_info.net_assets / stock.outstanding_shares, 2)
        pe_ratio = round(stock_in_market.price / eps, 2)
        valuation["valuation"] = {
            "pe_ratio": pe_ratio,
            "net_asset_per_share": naps,
            "eps": eps,
            "dividend_yield": period,
        }
        valuation["company_statistics"] = {
            "registrars": stock.registrar,
            "listing_date": stock.list_date,
            "year_end": stock.year_end,
            "share_outstanding": stock.outstanding_shares,
        }
        valuation["kpi"] = {
            "turnover_growth": round(
                (
                    (
                        stock_analytics_info.turnover
                        - stock_analytics_info.previous_turnover
                    )
                    / stock_analytics_info.previous_turnover
                )
                * 100,
                2,
            ),
            "pat_growth": round(
                (
                    (
                        stock_analytics_info.profit_after_tax
                        - stock_analytics_info.previous_profit_after_tax
                    )
                    / stock_analytics_info.previous_profit_after_tax
                )
                * 100,
                2,
            ),
            "net_assets_growth": round(
                (
                    (
                        stock_analytics_info.net_assets
                        - stock_analytics_info.previous_net_assets
                    )
                    / stock_analytics_info.previous_net_assets
                )
                * 100,
                2,
            ),
            "assets_growth": round(
                (
                    (
                        stock_analytics_info.total_assets
                        - stock_analytics_info.previous_total_assets
                    )
                    / stock_analytics_info.previous_total_assets
                )
                * 100,
                2,
            ),
        }
    return valuation


def stock_competitors(query_params):
    """
    Return list of all competitors to current stock

    :param query_params: query parameters on the url
    :return: list of all competitors stock
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
