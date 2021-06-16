# Generated by Django 3.1.1 on 2020-10-24 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0094_auto_20201024_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='quiz',
            field=models.BooleanField(blank=True, default=False, verbose_name='quiz given?'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 24, 13, 44, 20, 657545), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 24, 13, 44, 20, 657515), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 24, 13, 44, 20, 656863), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='KAFSZCFG', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 24, 13, 44, 20, 646333), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 24, 13, 44, 20, 646294), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]
