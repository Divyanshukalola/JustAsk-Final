# Generated by Django 3.0.4 on 2020-09-05 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_auto_20200904_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='First',
            field=models.BooleanField(blank=True, default=True, verbose_name='First Time?'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 13, 5, 12, 842685), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='DNNR919S', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 13, 5, 12, 832679), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 13, 5, 12, 832679), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]
