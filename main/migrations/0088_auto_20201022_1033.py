# Generated by Django 3.1.1 on 2020-10-22 10:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0087_auto_20201021_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
            ],
        ),
        migrations.AlterField(
            model_name='buybook',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 22, 10, 33, 1, 437673), null=True, verbose_name='End Date of Rental book'),
        ),
        migrations.AlterField(
            model_name='buybook',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 22, 10, 33, 1, 437636), null=True, verbose_name='Start Date Rental book'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 22, 10, 33, 1, 437054), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='58R1XA2C', max_length=8, unique=True, verbose_name='Question ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='EndDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 22, 10, 33, 1, 427858), null=True, verbose_name='End Date of Subscription'),
        ),
        migrations.AlterField(
            model_name='student',
            name='StartDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 22, 10, 33, 1, 427822), null=True, verbose_name='Start Date of Subscription'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField(verbose_name='choice')),
                ('is_answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.quizequestion')),
            ],
        ),
    ]