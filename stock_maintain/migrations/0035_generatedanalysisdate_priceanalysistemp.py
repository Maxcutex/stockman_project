# Generated by Django 2.1.4 on 2020-03-29 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_setup_info', '0030_auto_20200322_1403'),
        ('stock_maintain', '0034_auto_20200326_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedAnalysisDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_generated_for', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceAnalysisTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_code', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('min_year', models.FloatField()),
                ('max_year', models.FloatField()),
                ('min_six_months', models.FloatField()),
                ('max_six_months', models.FloatField()),
                ('min_three_months', models.FloatField()),
                ('max_three_months', models.FloatField()),
                ('min_one_week', models.FloatField()),
                ('max_one_week', models.FloatField()),
                ('price_one_week', models.FloatField()),
                ('price_three_months', models.FloatField()),
                ('price_six_months', models.FloatField()),
                ('price_one_year', models.FloatField()),
                ('one_week_cent', models.FloatField()),
                ('three_months_cent', models.FloatField()),
                ('six_months_cent', models.FloatField()),
                ('one_year_cent', models.FloatField()),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_analysi_stock', to='stock_setup_info.Stock')),
            ],
        ),
    ]