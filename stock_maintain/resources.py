from .models import (
    PriceList,
    AsiIndex,
    Quote,
    BonusTracker,
    DailyMarketIndex,
    Dividend,
    News,
    NewsImage,
    OfferIpo,
)
from import_export import resources


class PriceListResource(resources.ModelResource):
    class Meta:
        model = PriceList
        exclude = ("id",)
        fields = (
            "sec_code",
            "price_date",
            "price_close",
            "x_open",
            "x_high",
            "x_low",
            "price",
            "offer_bid_sign",
            "x_change",
            "num_of_deals",
            "volume",
            "x_value",
            "x_change",
        )


class AsiIndexResource(resources.ModelResource):
    class Meta:
        model = AsiIndex


class QuotesResource(resources.ModelResource):
    class Meta:
        model = Quote


class BonusTrackerResource(resources.ModelResource):
    class Meta:
        model = BonusTracker


class DailyMarketIndexResource(resources.ModelResource):
    class Meta:
        model = DailyMarketIndex


class DividendResource(resources.ModelResource):
    class Meta:
        model = Dividend


class NewsResource(resources.ModelResource):
    class Meta:
        model = News


class NewsImagesResource(resources.ModelResource):
    class Meta:
        model = NewsImage


class OfferIpoResource(resources.ModelResource):
    class Meta:
        model = OfferIpo
