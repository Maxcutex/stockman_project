from django.contrib import admin

from stock_maintain import models
from .resources import PriceListResource
from .models import (PriceList, AsiIndex, Quote,
                     BonusTracker, DailyMarketIndex, Dividend, News, NewsImage, OfferIpo, )
from import_export.admin import ImportExportModelAdmin

# admin.site.register(PriceList)


@admin.register(PriceList)
class PriceListAdmin(ImportExportModelAdmin):
    pass


@admin.register(AsiIndex)
class AsiIndexAdmin(ImportExportModelAdmin):
    pass


@admin.register(Quote)
class QuoteAdmin(ImportExportModelAdmin):
    pass


@admin.register(BonusTracker)
class BonusTrackerAdmin(ImportExportModelAdmin):
    pass


@admin.register(DailyMarketIndex)
class DailyMarketIndexAdmin(ImportExportModelAdmin):
    pass


@admin.register(Dividend)
class DividendAdmin(ImportExportModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    model = models.News
    list_display = ('excerpt',)

    def excerpt(self, obj):
        return obj.get_summary(5)


@admin.register(NewsImage)
class NewsImageAdmin(ImportExportModelAdmin):
    pass


@admin.register(OfferIpo)
class OfferIpoAdmin(ImportExportModelAdmin):
    pass
