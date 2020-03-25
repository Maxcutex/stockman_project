# Generated by Django 2.1.4 on 2020-02-23 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_setup_info', '0028_auto_20191212_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmanagement',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='management_stock', to='stock_setup_info.Stock'),
            preserve_default=False,
        ),
    ]