# Generated by Django 3.0.4 on 2020-08-30 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200831_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 31, 0, 40, 46, 173001), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='LACE1VU3', max_length=8, unique=True, verbose_name='Question ID'),
        ),
    ]