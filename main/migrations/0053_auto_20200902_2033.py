# Generated by Django 3.0.4 on 2020-09-02 15:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0052_auto_20200902_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='BookBuy', to='main.EBook'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 20, 33, 35, 580218), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='JIEJNHRU', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 20, 33, 35, 568250), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 20, 33, 35, 568250), null=True, verbose_name='Start Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='made_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
