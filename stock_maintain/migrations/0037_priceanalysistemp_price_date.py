# Generated by Django 2.1.4 on 2020-04-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_maintain', '0036_auto_20200330_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceanalysistemp',
            name='price_date',
            field=models.DateTimeField(null=True),
        ),
    ]
