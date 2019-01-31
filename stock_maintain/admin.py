from django.contrib import admin
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse

from stock_maintain import models
from .resources import PriceListResource
from .models import (PriceList, AsiIndex, Quote,
					 BonusTracker, DailyMarketIndex, Dividend, News, NewsImage, OfferIpo, NewsFile, NewsCategorySection,
					 AnalysisOpinion, AnalysisCategorySection, Author)
from import_export.admin import ImportExportModelAdmin


def get_picture_preview(obj):
	if obj.pk:  # if object has already been saved and has a primary key, show picture preview
		return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
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
		if obj.pk:  # if object has already been saved and has a primary key, show link to it
			url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
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


class AuthorInline(admin.TabularInline):
	model = Author
	extra = 1
	fields = ["is_main", "name", "doc_type", "doc_file"]


class NewsSectionInline(admin.TabularInline):
	model = NewsCategorySection
	extra = 0
	fields = ["news", "section"]


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


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
	pass


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
	model = models.News
	inlines = [NewsImageInline, NewsFileInline, NewsSectionInline, AuthorInline]
	list_display = ('excerpt',)

	def excerpt(self, obj):
		return obj.get_summary(5)


@admin.register(NewsImage)
class NewsImageAdmin(ImportExportModelAdmin):
	pass


@admin.register(OfferIpo)
class OfferIpoAdmin(ImportExportModelAdmin):
	pass


class AnalysisOpinionSectionInline(admin.TabularInline):
	model = AnalysisCategorySection
	extra = 0
	fields = ["analysis", "section"]


@admin.register(AnalysisOpinion)
class AnalysisOpinionAdmin(ImportExportModelAdmin):
	model = models.AnalysisOpinion
	inlines = [AnalysisOpinionSectionInline]
