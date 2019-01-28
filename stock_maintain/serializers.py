from rest_framework import serializers
from enumchoicefield import ChoiceEnum, EnumChoiceField

from stock_setup_info.serializers import StructureSerializer
from .models import (PriceList, AsiIndex, Quote,
					 BonusTracker, DailyMarketIndex, Dividend, News, NewsImage, OfferIpo, OfferMethod, OfferType,
					 NewsCategorySection, AnalysisOpinion, AnalysisCategorySection)


class PriceListSerializer(serializers.ModelSerializer):
	class Meta:
		model = PriceList
		fields = (
			'id', 'sec_code', 'price_date',
			'price_close', 'x_open', 'x_high',
			'x_low', 'price', 'offer_bid_sign',
			'x_change', 'num_of_deals', 'volume',
			'x_value', 'dps', 'eps',
			'pe', 'rpt', 'e_time',
			'e_date', 'source', 'sync_flag', 'stock'
		)
		ordering_fields = ('id',)
		ordering = ['-id']


class AsiIndexSerializer(serializers.ModelSerializer):
	class Meta:
		model = AsiIndex
		fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quote
		fields = '__all__'


class BonusTrackerSerializer(serializers.ModelSerializer):
	class Meta:
		model = BonusTracker
		fields = '__all__'


class DailyMarketIndexSerializer(serializers.ModelSerializer):
	class Meta:
		model = DailyMarketIndex
		fields = '__all__'


class DividendSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dividend
		fields = '__all__'


class NewsImageSerializer(serializers.ModelSerializer):
	image_file = serializers.ImageField(max_length=None, use_url=True)

	class Meta:
		model = NewsImage
		fields = '__all__'


class NewsFileSerializer(serializers.ModelSerializer):
	doc_file = serializers.FileField(max_length=None, use_url=True)

	class Meta:
		model = NewsImage
		fields = '__all__'


class NewsCategorySectionSerializer(serializers.ModelSerializer):
	section = StructureSerializer(read_only=True)

	class Meta:
		model = NewsCategorySection
		fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
	visual_news = NewsImageSerializer(many=True, read_only=True)
	doc_news = NewsFileSerializer(many=True, read_only=True)
	category_news = NewsCategorySectionSerializer(many=True, read_only=True)

	class Meta:
		model = News
		fields = '__all__'
		ordering_fields = ('id',)
		ordering = ['-id']


class AnalysisCategorySectionSerializer(serializers.ModelSerializer):
	category_analysis_structure = StructureSerializer(many=True, read_only=True)

	class Meta:
		model = AnalysisCategorySection
		fields = '__all__'
		ordering_fields = ('id',)
		ordering = ['-id']


class AnalysisOpinionSerializer(serializers.ModelSerializer):
	analysis_news = AnalysisCategorySectionSerializer(many=True, read_only=True)

	class Meta:
		model = AnalysisOpinion
		fields = '__all__'
		ordering_fields = ('id',)
		ordering = ['-id']
