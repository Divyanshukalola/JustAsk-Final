# Generated by Django 3.0.4 on 2020-08-30 10:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200829_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Question'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 30, 15, 44, 44, 889705), null=True, verbose_name='Date Of Paper'),
        ),
    ]
