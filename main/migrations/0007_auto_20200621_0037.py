# Generated by Django 3.0.4 on 2020-06-20 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200621_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='design_designer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 0, 37, 54, 550792), verbose_name='date published'),
        ),
    ]
