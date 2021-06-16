# Generated by Django 3.1.1 on 2020-11-11 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0101_auto_20201111_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='searche',
            name='user',
            field=models.CharField(blank=True, default='', max_length=700, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 171489), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 171431), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 169807), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='5YBCU11I', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='searche',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 157052), null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 151134), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 2, 33, 22, 151071), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]