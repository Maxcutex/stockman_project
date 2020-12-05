# Generated by Django 2.1.4 on 2019-12-12 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0027_auto_20191211_1019"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="sub_sector",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stock_sub_sector",
                to="stock_setup_info.SubSector",
            ),
        ),
    ]
