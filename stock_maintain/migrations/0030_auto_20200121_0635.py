# Generated by Django 2.1.4 on 2020-01-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_maintain', '0029_auto_20191228_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='sec_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]