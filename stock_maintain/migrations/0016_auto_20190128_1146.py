# Generated by Django 2.1.4 on 2019-01-28 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0015_auto_20190127_1842"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysiscategorysection",
            name="analysis",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category_analysis",
                to="stock_maintain.AnalysisOpinion",
            ),
        ),
    ]
