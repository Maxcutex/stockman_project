# Generated by Django 2.1.4 on 2020-03-22 14:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0029_stockmanagement_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
