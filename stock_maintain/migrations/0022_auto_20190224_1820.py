# Generated by Django 2.1.4 on 2019-02-24 18:20

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('stock_maintain', '0021_auto_20190224_1808'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='SiteAuthor',
        ),
    ]
