# Generated by Django 2.1.4 on 2018-12-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0010_auto_20181231_0737"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="list_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="regis_close",
            field=models.DateField(blank=True, null=True),
        ),
    ]
