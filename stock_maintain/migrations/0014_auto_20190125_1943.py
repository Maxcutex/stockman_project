# Generated by Django 2.1.4 on 2019-01-25 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0013_auto_20190125_1333"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="date",
            new_name="news_date",
        ),
        migrations.RenameField(
            model_name="news",
            old_name="stock_id",
            new_name="stock",
        ),
    ]
