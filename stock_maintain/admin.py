import io
import pdb
from datetime import datetime
import logging
from django.db import connection
from django.contrib import messages
from django.contrib import admin
from django.db import transaction
from django.forms import forms
from stockman_project.celery import refresh_analysis_data, process_csv_upload_task

from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from psycopg2._psycopg import IntegrityError
from rest_framework.reverse import reverse
import csv
from stock_maintain import models
from stock_setup_info.models import SectionGroup, Stock
from .resources import PriceListResource
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
    NewsFile,
    NewsCategorySection,
    AnalysisOpinion,
    AnalysisCategorySection,
    SiteAuthor,
    InsideBusiness,
    InsideBusinessSection,
    AnalysisImage,
    AnalysisFile,
    InsideBusinessImage,
    InsideBusinessFile,
    QuarterlyFinancial,
    DividendInformation,
    PriceAnalysisTemp,
)
from import_export.admin import ImportExportModelAdmin
from django.urls import path

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_picture_preview(obj):
    if (
        obj.pk
    ):  # if object has already been saved and has a primary key, show picture preview
        return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}"
        style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.image_file.url,
            title=obj.name,
        )
    return _("(choose a picture and save and continue editing to see the preview)")


get_picture_preview.allow_tags = True
get_picture_preview.short_description = _("Picture Preview")


# admin.site.register(PriceList)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ["is_main", "name", "image_type", "image_file", get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if (
            obj.pk
        ):  # if object has already been saved and has a primary key, show link to it
            url = reverse(
                "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
                args=[force_text(obj.pk)],
            )
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")

    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True


class NewsFileInline(admin.TabularInline):
    model = NewsFile
    extra = 0
    fields = ["is_main", "name", "doc_type", "doc_file"]


class NewsSectionInline(admin.TabularInline):
    model = NewsCategorySection
    extra = 0
    fields = ["news", "section_category"]


class AnalysisImageInline(admin.TabularInline):
    model = AnalysisImage
    extra = 1
    fields = ["is_main", "name", "image_type", "image_file", get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if (
            obj.pk
        ):  # if object has already been saved and has a primary key, show link to it
            url = reverse(
                "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
                args=[force_text(obj.pk)],
            )
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")

    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True


class AnalysisFileInline(admin.TabularInline):
    model = AnalysisFile
    extra = 0
    fields = ["is_main", "name", "doc_type", "doc_file"]


class InsideBusinessImageInline(admin.TabularInline):
    model = InsideBusinessImage
    extra = 1
    fields = ["is_main", "name", "image_type", "image_file", get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if (
            obj.pk
        ):  # if object has already been saved and has a primary key, show link to it
            url = reverse(
                "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
                args=[force_text(obj.pk)],
            )
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")

    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True


class InsideBusinessFileInline(admin.TabularInline):
    model = InsideBusinessFile
    extra = 0
    fields = ["is_main", "name", "doc_type", "doc_file"]


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    date_import = forms.Field()


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    # class PriceListAdmin(ImportExportModelAdmin):
    list_display = (
        "sec_code",
        "price_date",
        "price",
        "x_open",
        "x_high",
        "x_low",
        "price_close",
        "offer_bid_sign",
        "x_change",
        "x_value",
    )
    search_fields = (
        "sec_code",
        "price_date",
    )
    # price_close = models.FloatField()
    # x_open = models.FloatField()
    # x_high = models.FloatField()
    # x_low = models.FloatField()
    # price = models.FloatField()
    # offer_bid_sign = models.CharField(max_length=5)
    # x_change = models.FloatField()
    # resource_class = PriceListResource
    change_list_template = "entities/pricelists_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import-csv/", self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        """

        :param request:
        :type request:
        :return:
        :rtype:
        """

        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            print("importing file ....")
            logger.info("importing file ....")
            date_import = request.POST["date_import"]
            import boto3

            s3 = boto3.resource("s3")
            s3.meta.client.upload_file(csv_file, "csv_uploads", f"{date_import}.csv")

            # process_csv_upload_task.delay(date_import)
            self.message_user(
                request,
                "Your csv file is imported and currently being processed. You will be notified when its done",
            )

        print("successful")
        logger.info("successful importing file ....")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)


@admin.register(AsiIndex)
class AsiIndexAdmin(ImportExportModelAdmin):
    """"""

    pass


@admin.register(Quote)
class QuoteAdmin(ImportExportModelAdmin):
    pass


@admin.register(BonusTracker)
class BonusTrackerAdmin(ImportExportModelAdmin):
    pass


@admin.register(SectionGroup)
class SectionGroupAdmin(ImportExportModelAdmin):
    model = models.SectionGroup


@admin.register(DailyMarketIndex)
class DailyMarketIndexAdmin(ImportExportModelAdmin):
    pass


@admin.register(Dividend)
class DividendAdmin(ImportExportModelAdmin):
    pass


@admin.register(SiteAuthor)
class SiteAuthorAdmin(ImportExportModelAdmin):
    pass


@admin.register(NewsCategorySection)
class NewsCategorySectionAdmin(ImportExportModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    model = models.News
    inlines = [NewsImageInline, NewsFileInline, NewsSectionInline]
    search_fields = (
        "title",
        "description",
    )
    list_display = ("newstitle",)

    def newstitle(self, obj):
        return obj.title


@admin.register(NewsImage)
class NewsImageAdmin(ImportExportModelAdmin):
    pass


@admin.register(OfferIpo)
class OfferIpoAdmin(ImportExportModelAdmin):
    pass


class AnalysisOpinionSectionInline(admin.TabularInline):
    model = AnalysisCategorySection
    extra = 0
    fields = ["analysis", "section_category"]


@admin.register(AnalysisOpinion)
class AnalysisOpinionAdmin(ImportExportModelAdmin):
    model = models.AnalysisOpinion
    inlines = [AnalysisOpinionSectionInline, AnalysisImageInline, AnalysisFileInline]
    search_fields = (
        "title",
        "description",
    )
    list_display = ("titles",)

    def titles(self, obj):
        return obj.title


class InsideBusinessInline(admin.TabularInline):
    model = InsideBusinessSection
    extra = 0
    fields = ["inside_business", "section_category"]


@admin.register(InsideBusiness)
class InsideBusinessAdmin(ImportExportModelAdmin):
    model = models.InsideBusiness
    inlines = [
        InsideBusinessInline,
        InsideBusinessImageInline,
        InsideBusinessFileInline,
    ]
    search_fields = (
        "title",
        "description",
    )
    list_display = ("titles",)

    def titles(self, obj):
        return obj.title


@admin.register(QuarterlyFinancial)
class QuarterlyFinancialAdmin(ImportExportModelAdmin):
    model = models.QuarterlyFinancial

    search_fields = (
        "sec_code",
        "stock.stock_code",
    )
    list_display = ("titles",)

    def titles(self, obj):
        return obj.stock.stock_code


@admin.register(PriceAnalysisTemp)
class PriceAnalysisTempAdmin(ImportExportModelAdmin):
    pass


@admin.register(DividendInformation)
class DividendInformationAdmin(ImportExportModelAdmin):
    model = models.DividendInformation

    search_fields = (
        "sec_code",
        "stock.stock_code",
    )
    list_display = ("titles",)

    def titles(self, obj):
        return obj.stock.stock_code
