# Generated by Django 2.1.4 on 2019-01-30 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_maintain', '0016_auto_20190128_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('image_file', models.ImageField(blank=True, upload_to='images/analysis_image')),
                ('name', models.CharField(max_length=100)),
                ('image_type', models.CharField(choices=[('size930x620', 'size930x620'), ('size450x330', 'size450x330'), ('size300x200', 'size300x200')], default='size930x620', max_length=30)),
                ('analysis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visual_analysis', to='stock_maintain.AnalysisOpinion')),
            ],
        ),
    ]
