# Generated by Django 3.1.1 on 2020-11-09 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0099_auto_20201101_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searche',
            name='student',
        ),
    ]
