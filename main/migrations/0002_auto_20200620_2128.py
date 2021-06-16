# Generated by Django 3.0.4 on 2020-06-20 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='design_cover',
            field=models.ImageField(default='/covers/df.png', upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 21, 28, 14, 193013), verbose_name='date published'),
        ),
    ]
