# Generated by Django 2.1.4 on 2019-01-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0010_auto_20190113_1430"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricelist",
            name="x_change",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
