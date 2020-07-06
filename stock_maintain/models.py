from django.db import models, connection
from enumchoicefield import ChoiceEnum, EnumChoiceField
from stock_setup_info.models import Stock, Structure, SectionGroup
from model_utils import Choices
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class PriceList(models.Model):
    sec_code = models.CharField(max_length=100)
    price_date = models.DateField()
    price_close = models.FloatField()
    x_open = models.FloatField()
    x_high = models.FloatField()
    x_low = models.FloatField()
    price = models.FloatField()
    offer_bid_sign = models.CharField(max_length=5)
    x_change = models.FloatField()
    num_of_deals = models.FloatField()
    volume = models.FloatField()
    x_value = models.FloatField()
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='price_stock', null=True)

    def __str__(self):
        return self.sec_code

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class Quote(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='quotes_stock', null=True)
    sec_code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.sec_code


class AsiIndex(models.Model):
    date = models.DateField()
    price_close = models.FloatField()
    price_open = models.FloatField()
    price_high = models.FloatField()
    price_low = models.FloatField()
    price_close = models.FloatField()
    price_current = models.FloatField(null=True)

    def __str__(self):
        return self.date


class BonusTracker(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='bonus_stock', null=True)
    sec_code = models.CharField(max_length=10)
    bonus_val = models.SmallIntegerField()
    bonus_aggregate = models.SmallIntegerField()
    date_declared = models.DateField()

    def __str__(self):
        return self.sec_code


class DailyMarketIndex(models.Model):
    date = models.DateField()
    index = models.FloatField()
    deals = models.FloatField()
    volume = models.FloatField()
    value = models.FloatField()
    capital = models.FloatField()

    def __str__(self):
        return self.date


class QuarterType(ChoiceEnum):
    first_quarter = "first_quarter"
    second_quarter = "second_quarter"
    third_quarter = "third_quarter"
    fourth_quarter = "fourth_quarter"


class ImageSizeType(ChoiceEnum):
    size930x620 = "size930x620"
    size450x330 = "size450x330"


class Dividend(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='dividend_stock', null=True)
    sec_code = models.CharField(max_length=10)
    quarter_type = EnumChoiceField(
        QuarterType, default=QuarterType.first_quarter)
    interim = models.FloatField()
    bonus = models.FloatField()

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class SiteAuthor(models.Model):
    image_file = models.ImageField(blank=True, upload_to="images/authors_image")
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    description = RichTextUploadingField()
    twitter = models.CharField(max_length=150, null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    linked_in = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.first_name


class News(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    news_date = models.DateField()
    entry_date = models.DateField()
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='news_stock', null=True)
    sec_code = models.CharField(max_length=10, null=True)
    is_featured = models.BooleanField()
    has_downloadable = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    author = models.ForeignKey(
        SiteAuthor, on_delete=models.CASCADE, related_name='news_author', null=True, blank=True)

    def get_summary(self, char):
        return self.content[:char]

    def __str__(self):
        return self.title

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))

    @property
    def stock_indexing(self):
        """Stock for indexing.		Used in Elasticsearch indexing.		"""
        if self.stock is not None:
            return self.stock.name

    @property
    def author_indexing(self):
        """Publisher for indexing. Used in Elasticsearch indexing. """
        if self.author is not None:
            return self.author.first_name + ' ' + self.author.last_name


class NewsImage(models.Model):
    image_choice = Choices('size930x620', 'size450x330', 'size300x200', 'size330x220', 'size158x158')
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='visual_news', null=True)
    is_main = models.BooleanField()
    image_file = models.ImageField(blank=True, upload_to="images/news_image")
    name = models.CharField(max_length=100)
    image_type = models.CharField(
        choices=image_choice, default=image_choice.size930x620, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class NewsFile(models.Model):
    doc_choices = Choices('pdf', 'word', 'excel')
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='doc_news', null=True)
    is_main = models.BooleanField()
    doc_file = models.FileField(blank=True, upload_to="files/news_docs")
    name = models.CharField(max_length=100)
    doc_type = models.CharField(
        choices=doc_choices, default=doc_choices.pdf, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class OfferType(ChoiceEnum):
    hipo = "Hybrid Inital Public Offer"
    hpo = "Hybrid Public Offer"
    ipo = "Initial Public Offering"
    po = "Public Offer"
    ri = "Rights Issue"


class OfferMethod(ChoiceEnum):
    sal = "Offer For Sale"
    sub = "Offer For Subscription"
    ri = "Rights Issue"


class OfferIpo(models.Model):
    company_name = models.CharField(max_length=150)
    country_id = models.ForeignKey(
        Structure, on_delete=models.CASCADE, related_name='country', null=True)
    exchange_code = models.CharField(max_length=10)
    offer_type = EnumChoiceField(
        OfferType, default=OfferType.ipo)
    quarter_type = EnumChoiceField(
        OfferMethod, default=OfferMethod.sal)
    open_date = models.DateField(null=True)
    close_date = models.DateField(null=True)
    extended_date = models.DateField(null=True)
    proposed_listing_date = models.DateField(null=True)
    actual_listing_date = models.DateField(null=True)

    def __str__(self):
        return self.company_name


class NewsCategorySection(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='category_news', null=True)
    section_category = models.ForeignKey(
        SectionGroup, on_delete=models.CASCADE, related_name='category_news_section', null=True)

    def __str__(self):
        return self.section_category.section_name


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class AnalysisOpinion(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    opinion_date = models.DateField()
    entry_date = models.DateField()
    author = models.ForeignKey(
        SiteAuthor, on_delete=models.CASCADE, related_name='analysis_author', null=True)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class AnalysisFile(models.Model):
    doc_choices = Choices('pdf', 'word', 'excel')
    analysis = models.ForeignKey(
        AnalysisOpinion, on_delete=models.CASCADE, related_name='doc_analysis', null=True)
    is_main = models.BooleanField()
    doc_file = models.FileField(blank=True, upload_to="files/analysis_docs")
    name = models.CharField(max_length=100)
    doc_type = models.CharField(
        choices=doc_choices, default=doc_choices.pdf, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class AnalysisCategorySection(models.Model):
    analysis = models.ForeignKey(
        AnalysisOpinion, on_delete=models.CASCADE, related_name='category_analysis', null=True)
    section_category = models.ForeignKey(
        SectionGroup, on_delete=models.CASCADE, related_name='category_analysis_section', null=True)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class AnalysisImage(models.Model):
    image_choice = Choices('size930x620', 'size450x330', 'size300x200', 'size330x220', 'size158x158')
    analysis = models.ForeignKey(
        AnalysisOpinion, on_delete=models.CASCADE, related_name='visual_analysis', null=True)
    is_main = models.BooleanField()
    image_file = models.ImageField(blank=True, upload_to="images/analysis_image")
    name = models.CharField(max_length=100)
    image_type = models.CharField(
        choices=image_choice, default=image_choice.size930x620, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class InsideBusiness(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    opinion_date = models.DateField()
    entry_date = models.DateField()
    author = models.ForeignKey(
        SiteAuthor, on_delete=models.CASCADE, related_name='inside_business_author', null=True)

    def __str__(self):
        return self.title

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class InsideBusinessSection(models.Model):
    inside_business = models.ForeignKey(
        InsideBusiness, on_delete=models.CASCADE, related_name='category_inside_business', null=True)
    section_category = models.ForeignKey(
        SectionGroup, on_delete=models.CASCADE, related_name='category_inside_business_section', null=True)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class InsideBusinessFile(models.Model):
    doc_choices = Choices('pdf', 'word', 'excel')
    inside_business = models.ForeignKey(
        InsideBusiness, on_delete=models.CASCADE, related_name='doc_inside_business', null=True)
    is_main = models.BooleanField()
    doc_file = models.FileField(blank=True, upload_to="files/inside_business_docs")
    name = models.CharField(max_length=100)
    doc_type = models.CharField(
        choices=doc_choices, default=doc_choices.pdf, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class InsideBusinessImage(models.Model):
    image_choice = Choices('size930x620', 'size450x330', 'size300x200', 'size330x220', 'size158x158')
    inside_business = models.ForeignKey(
        InsideBusiness, on_delete=models.CASCADE, related_name='visual_inside_business', null=True)
    is_main = models.BooleanField()
    image_file = models.ImageField(blank=True, upload_to="images/inside_business_image")
    name = models.CharField(max_length=100)
    image_type = models.CharField(
        choices=image_choice, default=image_choice.size930x620, max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class NewsLetterMailing(models.Model):
    email = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()


class GeneratedAnalysisDate(models.Model):
    date_generated_for = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class PriceAnalysisTemp(models.Model):
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='temp_analysi_stock', null=True)
    sec_code = models.CharField(max_length=100)
    price = models.FloatField()
    min_year = models.FloatField(null=True)
    max_year = models.FloatField(null=True)
    min_six_months = models.FloatField(null=True)
    max_six_months = models.FloatField(null=True)
    min_three_months = models.FloatField(null=True)
    max_three_months = models.FloatField(null=True)
    min_one_week = models.FloatField(null=True)
    max_one_week = models.FloatField(null=True)

    price_one_week = models.FloatField(null=True)
    price_three_months = models.FloatField(null=True)
    price_six_months = models.FloatField(null=True)
    price_one_year = models.FloatField(null=True)

    one_week_cent = models.FloatField(null=True)
    three_months_cent = models.FloatField(null=True)
    six_months_cent = models.FloatField(null=True)
    one_year_cent = models.FloatField(null=True)
    price_date = models.DateTimeField(null=True)



