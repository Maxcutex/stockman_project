# Generated by Django 2.1.4 on 2018-12-23 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock_setup_info", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Structure",
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
                ("structure_name", models.CharField(max_length=100)),
                ("structure_code", models.CharField(max_length=50)),
                ("parent_id", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(max_length=100)),
                ("comment", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="StructureRelationship",
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
                    "from_structure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_structures",
                        to="stock_setup_info.Structure",
                    ),
                ),
                (
                    "to_structure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_structures",
                        to="stock_setup_info.Structure",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StructureType",
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
                ("structure_type_name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="StructureTypeRelationship",
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
                    "from_structure_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_structure_types",
                        to="stock_setup_info.Structure",
                    ),
                ),
                (
                    "to_structure_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_structure_types",
                        to="stock_setup_info.Structure",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="structuretype",
            name="structure_types",
            field=models.ManyToManyField(
                through="stock_setup_info.StructureTypeRelationship",
                to="stock_setup_info.StructureType",
            ),
        ),
        migrations.AddField(
            model_name="structure",
            name="structure_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="stock_setup_info.StructureType",
            ),
        ),
        migrations.AddField(
            model_name="structure",
            name="structures",
            field=models.ManyToManyField(
                through="stock_setup_info.StructureRelationship",
                to="stock_setup_info.Structure",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="structuretyperelationship",
            unique_together={("from_structure_type", "to_structure_type")},
        ),
        migrations.AlterUniqueTogether(
            name="structurerelationship",
            unique_together={("from_structure", "to_structure")},
        ),
    ]
