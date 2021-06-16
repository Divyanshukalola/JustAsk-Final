# Generated by Django 3.0.4 on 2020-09-01 08:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20200901_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksol',
            name='Ebook',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.EBook'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 13, 52, 7, 80121), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='EZIWDM7F', max_length=8, unique=True, verbose_name='Question ID'),
        ),
    ]