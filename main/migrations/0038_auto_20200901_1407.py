# Generated by Django 3.0.4 on 2020-09-01 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20200901_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='student',
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 14, 7, 44, 274070), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='X845GCKQ', max_length=8, unique=True, verbose_name='Question ID'),
        ),
    ]
