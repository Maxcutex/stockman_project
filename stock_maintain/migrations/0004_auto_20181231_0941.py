# Generated by Django 2.1.4 on 2018-12-31 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_maintain', '0003_auto_20181231_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='news_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visual_news', to='stock_maintain.News'),
        ),
    ]