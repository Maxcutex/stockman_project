# Generated by Django 2.1.4 on 2020-07-06 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0030_auto_20200322_1403"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="stock",
            options={"ordering": ["stock_code"]},
        ),
    ]
