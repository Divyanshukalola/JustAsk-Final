# Generated by Django 3.0.4 on 2020-09-05 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20200905_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='book_field',
            field=models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('science and engineering', 'SE - science and engineering'), ('social science and history', 'SS - social science and history'), ('language', 'LG - language'), ('business', 'BS - business')], default='other', max_length=200, verbose_name='Notes Field'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 14, 43, 0, 81387), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='IUTIB79Y', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 14, 43, 0, 75403), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 14, 43, 0, 75403), null=True, verbose_name='Start Date of Subscription'),
        ),
    ]
