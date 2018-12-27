from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from stock_setup_info.models import Stock, Structure
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
    num_of_deals = models.SmallIntegerField()
    volume = models.FloatField()
    x_value = models.FloatField()
    dps = models.FloatField()
    eps = models.FloatField()
    pe = models.FloatField()
    rpt = models.CharField(max_length=10)
    e_time = models.DateTimeField(max_length=10)
    e_date = models.DateField(max_length=10)
    source = models.CharField(max_length=20)
    sync_flag = models.SmallIntegerField()
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='price_stock', null=True)

    def __str__(self):
        return self.name


class Quotes(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='quotes_stock', null=True)
    sec_code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class AsiIndex(models.Model):
    date = models.DateField()
    price_close = models.FloatField()
    price_open = models.FloatField()
    price_high = models.FloatField()
    price_low = models.FloatField()
    price_close = models.FloatField()
    price_current = models.FloatField(null=True)


class BonusTracker(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='bonus_stock', null=True)
    sec_code = models.CharField(max_length=10)
    bonus_val = models.SmallIntegerField()
    bonus_aggregate = models.SmallIntegerField()
    date_declared = models.DateField()


class DailyMarketIndex(models.Model):
    date = models.DateField()
    index = models.FloatField()
    deals = models.FloatField()
    volume = models.FloatField()
    value = models.FloatField()
    capital = models.FloatField()


class QuarterType(ChoiceEnum):
    first_quarter = "first_quarter"
    second_quarter = "second_quarter"
    third_quarter = "third_quarter"
    fourth_quarter = "fourth_quarter"


class Dividend(models.Model):
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='dividend_stock', null=True)
    sec_code = models.CharField(max_length=10)
    quarter_type = EnumChoiceField(
        QuarterType, default=QuarterType.first_quarter)
    interim = models.FloatField()
    bonus = models.FloatField()


class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=10)
    news_section = models.ForeignKey(
        Structure, on_delete=models.CASCADE, related_name='news_structure')
    date = models.DateField()
    entry_date = models.DateField()
    stock_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='news_stock', null=True)
    sec_code = models.CharField(max_length=10)
    is_featured = models.BooleanField()
    author = models.CharField(max_length=100, null=True)


class NewsImages(models.Model):
    news_id = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='visual_news', null=True)
    is_main = models.BooleanField()
    image_file = models.FileField(blank=True, upload_to="images/news_image")
    name = models.CharField(max_length=100)


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
