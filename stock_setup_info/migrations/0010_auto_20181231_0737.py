# Generated by Django 2.1.4 on 2018-12-31 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_setup_info', '0009_stockmanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='structures', to='stock_setup_info.Structure'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='structure_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_structures', to='stock_setup_info.StructureType'),
        ),
        migrations.AlterField(
            model_name='structuretype',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_structure_type', to='stock_setup_info.StructureType'),
        ),
    ]