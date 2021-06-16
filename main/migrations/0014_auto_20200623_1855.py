# Generated by Django 3.0.4 on 2020-06-23 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200621_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nas_model', models.CharField(default='', max_length=200, verbose_name='Model')),
                ('nas_title', models.CharField(default='', max_length=200, verbose_name='Title')),
                ('nas_cover', models.ImageField(default='', upload_to='covers/', verbose_name='Cover Image')),
                ('nas_content_image1', models.ImageField(default='', upload_to='images/', verbose_name='Snapshot 1')),
                ('nas_content_image2', models.ImageField(default='', upload_to='images/', verbose_name='Snapshot 2')),
                ('nas_content_image3', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 3')),
                ('nas_content_image4', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 4')),
                ('nas_content_image5', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 5')),
                ('nas_content_image6', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 6')),
                ('nas_content_image7', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 7')),
                ('nas_content_image8', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 8')),
                ('nas_content_image9', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 9')),
                ('nas_content_image10', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Snapshot 10')),
                ('nas_description', models.TextField()),
                ('nas_price', models.PositiveSmallIntegerField(default=0, verbose_name='Price')),
            ],
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 18, 55, 10, 927355), verbose_name='date published'),
        ),
    ]