# Generated by Django 2.1.4 on 2020-10-28 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0031_auto_20200706_2028"),
        ("stock_maintain", "0040_auto_20201009_0024"),
    ]

    operations = [
        migrations.CreateModel(
            name="DividendInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sec_code", models.CharField(max_length=100)),
                ("dividend_type", models.IntegerField()),
                (
                    "period_number",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dividend_info_stock",
                        to="stock_setup_info.Stock",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuarterlyFinancial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sec_code", models.CharField(max_length=100)),
                ("profit_after_tax", models.FloatField()),
                ("turnover", models.FloatField()),
                ("net_assets", models.FloatField()),
                ("total_assets", models.FloatField()),
                ("year", models.IntegerField()),
                (
                    "period_number",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quarterly_fin_stock",
                        to="stock_setup_info.Stock",
                    ),
                ),
            ],
        ),
    ]
