from django.db import models

# Create your models here.


class PriceList(models.Model):
    sec_code = models.CharField(max_length=100)
    price_date = models.DateField(max_length=50)
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

    def __str__(self):
        return self.name
