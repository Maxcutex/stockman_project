# Generated by Django 2.1.4 on 2019-12-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_setup_info', '0026_sectiongroup'),
        ('stock_maintain', '0024_auto_20191201_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysiscategorysection',
            name='section',
        ),
        migrations.AddField(
            model_name='analysiscategorysection',
            name='section_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_analysis_section', to='stock_setup_info.SectionGroup'),
        ),
    ]
