# Generated by Django 3.0.4 on 2020-09-02 18:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_auto_20200902_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 23, 56, 57, 71461), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='3YHNLS77', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 23, 56, 57, 58498), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 2, 23, 56, 57, 58498), null=True, verbose_name='Start Date of Subscription'),
        ),
        migrations.CreateModel(
            name='SubsTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('applied', models.BooleanField(blank=True, default=False, verbose_name='applied?')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
            ],
        ),
    ]
