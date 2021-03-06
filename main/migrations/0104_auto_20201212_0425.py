# Generated by Django 3.1.1 on 2020-12-12 04:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0103_auto_20201208_0454'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 124143), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 124118), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 123519), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='8JQ36RYI', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='searche',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 117696), null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 113099), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 4, 25, 48, 113057), null=True, verbose_name='Start Date of Subscription'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.CharField(default='', max_length=2000, verbose_name='From Where?')),
                ('concern', models.CharField(default='', max_length=2000, verbose_name='Concerns about us?')),
                ('suggestions', models.CharField(default='', max_length=2000, verbose_name='suggestions?')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
