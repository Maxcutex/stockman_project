from rest_framework import serializers


from stock_setup_info.models import SectionGroup
from stock_setup_info.serializers import (
    SubSectorSerializer,
    MainSectorSerializer,
    StockSerializer,
)
from stockman_project.settings.base import MEDIA_URL
from .models import (
    PriceList,
    AsiIndex,
    Quote,
    BonusTracker,
    DailyMarketIndex,
    Dividend,
    News,
    NewsImage,
    NewsCategorySection,
    AnalysisOpinion,
    AnalysisCategorySection,
    SiteAuthor,
    InsideBusinessSection,
    InsideBusiness,
    InsideBusinessImage,
    NewsFile,
    InsideBusinessFile,
    AnalysisImage,
    NewsLetterMailing,
)


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class CustomPriceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sub_sector = SubSectorSerializer()
    main_sector = MainSectorSerializer()
    price_list = PriceListSerializer(many=True)
    sub_sector_name = serializers.CharField(max_length=200)
    main_sector_name = serializers.CharField(max_length=200)


class PriceListMarketAnalysisSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    sec_code = serializers.CharField()
    price = serializers.DecimalField(18, 2)
    min_year = serializers.DecimalField(18, 2)
    max_year = serializers.DecimalField(18, 2)
    min_six_months = serializers.DecimalField(18, 2)
    max_six_months = serializers.DecimalField(18, 2)
    min_three_months = serializers.DecimalField(18, 2)
    max_three_months = serializers.DecimalField(18, 2)
    min_one_week = serializers.DecimalField(18, 2)
    max_one_week = serializers.DecimalField(18, 2)
    one_week_cent = serializers.DecimalField(18, 2)
    three_months_cent = serializers.DecimalField(18, 2)
    six_months_cent = serializers.DecimalField(18, 2)
    one_year_cent = serializers.DecimalField(18, 2)


class SectionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionGroup
        fields = "__all__"


class AsiIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsiIndex
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class BonusTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusTracker
        fields = "__all__"


class DailyMarketIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMarketIndex
        fields = "__all__"


class DividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividend
        fields = "__all__"


class NewsImageSerializer(serializers.ModelSerializer):
    # image_file = serializers.ImageField(max_length=None, use_url=True)
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = NewsImage
        fields = "__all__"

    def get_image_file(self, NewsImage):
        request = self.context.get("request")
        image_file = NewsImage.image_file

        return request.build_absolute_uri(MEDIA_URL + str(image_file))


class InsideBusinessImageSerializer(serializers.ModelSerializer):
    # image_file = serializers.ImageField(max_length=None, use_url=True)
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = InsideBusinessImage
        fields = "__all__"

    def get_image_file(self, InsideBusinessImage):
        request = self.context.get("request")
        image_file = InsideBusinessImage.image_file
        return request.build_absolute_uri(MEDIA_URL + str(image_file))


class AnalysisImageSerializer(serializers.ModelSerializer):
    # image_file = serializers.ImageField(max_length=None, use_url=True)
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = AnalysisImage
        fields = "__all__"

    def get_image_file(self, InsideBusinessImage):
        request = self.context.get("request")
        image_file = InsideBusinessImage.image_file
        return request.build_absolute_uri(MEDIA_URL + str(image_file))


class NewsFileSerializer(serializers.ModelSerializer):
    doc_file = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = NewsFile
        fields = "__all__"


class AnalysisOpinionFileSerializer(serializers.ModelSerializer):
    doc_file = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = AnalysisOpinion
        fields = "__all__"


class InsideBusinessFileSerializer(serializers.ModelSerializer):
    doc_file = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = InsideBusinessFile
        fields = "__all__"


class NewsCategorySectionSerializer(serializers.ModelSerializer):
    section_category = SectionGroupSerializer(read_only=True)

    class Meta:
        model = NewsCategorySection
        fields = "__all__"


class SiteAuthorSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = SiteAuthor
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]

    def get_image_file(self, SiteAuthor):
        request = self.context.get("request")
        image_file = SiteAuthor.image_file
        return request.build_absolute_uri(MEDIA_URL + str(image_file))


class NewsSerializer(serializers.ModelSerializer):
    visual_news = NewsImageSerializer(many=True, read_only=True)
    doc_news = NewsFileSerializer(many=True, read_only=True)
    category_news = NewsCategorySectionSerializer(many=True, read_only=True)
    author = SiteAuthorSerializer(read_only=True)

    class Meta:
        model = News
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class AnalysisCategorySectionSerializer(serializers.ModelSerializer):
    section_category = SectionGroupSerializer(read_only=True)

    class Meta:
        model = AnalysisCategorySection
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class AnalysisOpinionSerializer(serializers.ModelSerializer):
    category_analysis = AnalysisCategorySectionSerializer(many=True, read_only=True)
    visual_analysis = AnalysisImageSerializer(many=True, read_only=True)
    author = SiteAuthorSerializer(read_only=True)
    doc_analysis = AnalysisOpinionFileSerializer(many=True, read_only=True)

    class Meta:
        model = AnalysisOpinion
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class InsideBusinessSectionSerializer(serializers.ModelSerializer):
    # visual_inside = InsideBusinessImageSerializer(many=True, read_only=True)
    # author = SiteAuthorSerializer(read_only=True)
    section_category = SectionGroupSerializer(read_only=True)

    class Meta:
        model = InsideBusinessSection
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class InsideBusinessSerializer(serializers.ModelSerializer):
    category_inside_business = InsideBusinessSectionSerializer(
        many=True, read_only=True
    )
    visual_inside_business = InsideBusinessImageSerializer(many=True, read_only=True)
    author = SiteAuthorSerializer(read_only=True)
    doc_inside_business = InsideBusinessFileSerializer(many=True, read_only=True)

    class Meta:
        model = InsideBusiness
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class NewsLetterMailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterMailing
        fields = "__all__"
        ordering_fields = ("id",)
        ordering = ["-id"]


class QuoteAnalysisSerializer(serializers.Serializer):
    market_analysis = PriceListMarketAnalysisSerializer()
    stock_details = StockSerializer()
