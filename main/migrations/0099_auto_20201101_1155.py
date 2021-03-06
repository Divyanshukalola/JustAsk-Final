# Generated by Django 3.1.1 on 2020-11-01 11:55

import datetime
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0098_auto_20201101_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', verbose_name='search')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 9, 4, 6, 39, 919539), null=True, verbose_name='Date')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
            ],
        )
    ]
