# Generated by Django 2.1.4 on 2019-01-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0020_auto_20190125_1143"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="contact",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="description",
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
