# Generated by Django 3.0.4 on 2020-06-20 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200620_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_cover',
            field=models.ImageField(default='/covers/df.png', upload_to='media/covers/'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 21, 58, 47, 225965), verbose_name='date published'),
        ),
    ]