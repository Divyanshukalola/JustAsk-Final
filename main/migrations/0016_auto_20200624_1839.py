# Generated by Django 3.0.4 on 2020-06-24 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200624_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=200, verbose_name='fname')),
                ('lname', models.CharField(default='', max_length=200, verbose_name='lname')),
                ('email', models.EmailField(default='', max_length=200, verbose_name='email')),
                ('pass1', models.CharField(default='', max_length=200, verbose_name='pass1')),
                ('pass2', models.CharField(default='', max_length=200, verbose_name='pass2')),
            ],
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 18, 39, 58, 291649), verbose_name='date published'),
        ),
    ]