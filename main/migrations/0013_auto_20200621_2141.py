# Generated by Django 3.0.4 on 2020-06-21 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200621_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='design_content_image10',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 10'),
        ),
        migrations.AddField(
            model_name='design',
            name='design_content_image6',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 6'),
        ),
        migrations.AddField(
            model_name='design',
            name='design_content_image7',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 7'),
        ),
        migrations.AddField(
            model_name='design',
            name='design_content_image8',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 8'),
        ),
        migrations.AddField(
            model_name='design',
            name='design_content_image9',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 9'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 21, 41, 36, 473331), verbose_name='date published'),
        ),
    ]