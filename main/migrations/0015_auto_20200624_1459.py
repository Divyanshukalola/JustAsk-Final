# Generated by Django 3.0.4 on 2020-06-24 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200623_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 14, 59, 58, 629998), verbose_name='date published'),
        ),
    ]