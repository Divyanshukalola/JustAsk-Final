# Generated by Django 3.0.4 on 2020-06-24 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200624_1842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MACKUsers',
            new_name='MACKUser',
        ),
        migrations.AlterField(
            model_name='design',
            name='design_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 18, 48, 27, 38386), verbose_name='date published'),
        ),
    ]
