# Generated by Django 2.1.4 on 2019-02-24 18:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0020_auto_20190224_1807"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
