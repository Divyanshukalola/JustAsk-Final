# Generated by Django 3.0.4 on 2020-08-31 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20200831_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='price',
            field=models.IntegerField(blank=True, default=450, verbose_name='Rental Price'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='price2',
            field=models.IntegerField(blank=True, default=650, verbose_name='Buy Price'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 31, 23, 47, 39, 852883), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='3B3YW6U8', max_length=8, unique=True, verbose_name='Question ID'),
        ),
    ]
