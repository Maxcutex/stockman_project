from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=100)
    exchange_code = models.CharField(max_length=50)
    sync_flag = models.CharField(max_length=30)
    logo = models.CharField(max_length=10)

    def __str__(self):
