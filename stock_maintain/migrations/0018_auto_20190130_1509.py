# Generated by Django 2.1.4 on 2019-01-30 15:09

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock_maintain", "0017_analysisimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_file",
                    models.ImageField(blank=True, upload_to="images/authors_image"),
                ),
                ("first_name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
                ("description", ckeditor_uploader.fields.RichTextUploadingField()),
                ("twitter", models.CharField(max_length=150)),
                ("facebook", models.CharField(max_length=150)),
                ("linked_in", models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name="analysisopinion",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="analysis_author",
                to="stock_maintain.Author",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news_author",
                to="stock_maintain.Author",
            ),
        ),
    ]
