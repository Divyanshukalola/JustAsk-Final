# Generated by Django 3.1.1 on 2020-10-16 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0083_auto_20201016_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='expert',
            field=models.BooleanField(blank=True, default=False, verbose_name='expert?'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 48, 15, 951755), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 48, 15, 951720), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 48, 15, 951101), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='TJKI4WU4', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 48, 15, 940984), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 16, 12, 48, 15, 940941), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]
