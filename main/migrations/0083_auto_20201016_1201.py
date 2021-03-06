# Generated by Django 3.1.1 on 2020-10-16 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0082_auto_20201012_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Answered?'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 1, 33, 172176), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 1, 33, 172145), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 1, 33, 171428), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='T9ABBEZ9', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 1, 33, 161316), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 1, 33, 161276), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]
