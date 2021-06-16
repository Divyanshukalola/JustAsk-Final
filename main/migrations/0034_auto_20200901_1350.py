# Generated by Django 3.0.4 on 2020-09-01 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20200831_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bcover', models.FileField(blank=True, default='', upload_to='ebook/', verbose_name='Book Cover')),
                ('File_name', models.CharField(default='', max_length=200, verbose_name='Title')),
                ('Edition', models.CharField(default='1st Edition', max_length=200, verbose_name='Edition')),
                ('book_field', models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('physical science and engineering', 'PE - physical science and engineering'), ('arts and designing', 'AD - arts and designing'), ('social science', 'SS - social science'), ('health', 'HL - health'), ('data science', 'DS - data science'), ('language', 'LG - language'), ('business', 'BS - business')], default='other', max_length=200, verbose_name='Book Field')),
                ('File', models.FileField(blank=True, default='', upload_to='ebook/', verbose_name='Solution(PDF)')),
                ('Auth', models.CharField(default='', max_length=200, verbose_name='Solution Author')),
                ('Description', models.TextField(default='', verbose_name='Body')),
            ],
        ),
        migrations.AlterField(
            model_name='paper',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 13, 50, 4, 46071), null=True, verbose_name='Date Of Paper'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(default='T5QJQMVB', max_length=8, unique=True, verbose_name='Question ID'),
        ),
    ]