from rest_framework import serializers
from enumchoicefield import ChoiceEnum, EnumChoiceField
from .models import (PriceList, AsiIndex, Quote,
					 BonusTracker, DailyMarketIndex, Dividend, News, NewsImage, OfferIpo, OfferMethod, OfferType,
					 )


class PriceListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PriceList
		fields = '__all__'


class AsiIndexSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AsiIndex
		fields = '__all__'


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
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


class NewsSerializer(serializers.ModelSerializer):
	visual_news = NewsImageSerializer(many=True, read_only=True)

	class Meta:
		model = News
		fields = '__all__'
