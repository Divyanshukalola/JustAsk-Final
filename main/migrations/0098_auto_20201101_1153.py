# Generated by Django 3.1.1 on 2020-11-01 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_auto_20201024_1443'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='booktransaction',
            name='amount',  
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 1, 11, 53, 42, 278762), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 1, 11, 53, 42, 278733), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 1, 11, 53, 42, 278079), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='X27TRI2Y', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 1, 11, 53, 42, 267814), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 1, 11, 53, 42, 267768), null=True, verbose_name='Start Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='substransaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]
