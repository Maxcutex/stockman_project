# Generated by Django 2.1.4 on 2018-12-31 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_setup_info', '0011_auto_20181231_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='view_count',
            field=models.BigIntegerField(default=0),
        ),
    ]