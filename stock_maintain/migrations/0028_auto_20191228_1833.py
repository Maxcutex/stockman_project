# Generated by Django 2.1.4 on 2019-12-28 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0027_analysisfile_insidebusinessfile_insidebusinessimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pricelist",
            name="dps",
        ),
        migrations.RemoveField(
            model_name="pricelist",
            name="eps",
        ),
        migrations.RemoveField(
            model_name="pricelist",
            name="pe",
        ),
    ]
