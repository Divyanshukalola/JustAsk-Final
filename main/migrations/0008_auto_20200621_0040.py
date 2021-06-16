# Generated by Django 3.0.4 on 2020-06-20 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200621_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_content_image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Model Snapshoots'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_cover',
            field=models.ImageField(default='', upload_to='covers/', verbose_name='Cover Image'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_designer',
            field=models.CharField(default='', max_length=200, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_price',
            field=models.PositiveSmallIntegerField(default=0.0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 0, 40, 56, 535751), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_title',
            field=models.CharField(default='', max_length=200, verbose_name='Title'),
        ),
    ]
