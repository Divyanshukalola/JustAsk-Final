# Generated by Django 3.0.4 on 2020-08-29 08:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200624_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='', verbose_name='Answer')),
                ('ans_file', models.FileField(blank=True, default='', upload_to='files/', verbose_name='Answer File')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Dislikes')),
            ],
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.CharField(default='', max_length=200, verbose_name='File Name')),
                ('book_field', models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('physical science and engineering', 'PE - physical science and engineering'), ('arts and designing', 'AD - arts and designing'), ('social science', 'SS - social science'), ('health', 'HL - health'), ('data science', 'DS - data science'), ('language', 'LG - language'), ('business', 'BS - business')], default='other', max_length=200, verbose_name='Book Field')),
                ('File', models.FileField(blank=True, default='', upload_to='ebook/', verbose_name='Ebook')),
                ('Auth', models.CharField(default='', max_length=200, verbose_name='Book Author')),
                ('BID', models.CharField(blank=True, default='', max_length=200, verbose_name='BOOK ID')),
                ('Description', models.TextField(default='', verbose_name='Body')),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.CharField(default='', max_length=200, verbose_name='File Name')),
                ('book_field', models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('physical science and engineering', 'PE - physical science and engineering'), ('arts and designing', 'AD - arts and designing'), ('social science', 'SS - social science'), ('health', 'HL - health'), ('data science', 'DS - data science'), ('language', 'LG - language'), ('business', 'BS - business')], default='other', max_length=200, verbose_name='Notes Field')),
                ('File', models.FileField(blank=True, default='', upload_to='notes/', verbose_name='Notes')),
                ('Auth', models.CharField(default='', max_length=200, verbose_name='Notes Author')),
                ('Description', models.TextField(default='', verbose_name='Body')),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='Price')),
                ('Chapter', models.CharField(blank=True, default='', max_length=200, verbose_name='Section/Chapter Number')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.CharField(default='', max_length=200, verbose_name='File Name')),
                ('book_field', models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('physical science and engineering', 'PE - physical science and engineering'), ('arts and designing', 'AD - arts and designing'), ('social science', 'SS - social science'), ('health', 'HL - health'), ('data science', 'DS - data science'), ('language', 'LG - language'), ('business', 'BS - business')], default='other', max_length=200, verbose_name="Paper's Field")),
                ('File', models.FileField(blank=True, default='', upload_to='notes/', verbose_name='Paper')),
                ('Date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 29, 14, 29, 5, 473542), null=True, verbose_name='Date Of Paper')),
                ('Description', models.TextField(default='', verbose_name='Body')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('question_field', models.CharField(choices=[('other', 'OT - other'), ('computer science', 'CS - computer science'), ('math', 'MT - math'), ('physical science and engineering', 'PE - physical science and engineering'), ('arts and designing', 'AD - arts and designing'), ('social science', 'SS - social science'), ('health', 'HL - health'), ('data science', 'DS - data science'), ('language', 'LG - language'), ('business', 'BS - business')], default='computer science', max_length=200, verbose_name='Course Field')),
                ('question_cover', models.ImageField(default='', upload_to='covers/', verbose_name='Cover Image')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, default='', max_length=200, verbose_name='First Name')),
                ('SecondName', models.CharField(blank=True, default='', max_length=200, verbose_name='Second Name')),
                ('Email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('Studentid', models.CharField(default='A20435927', max_length=9, unique=True, verbose_name='Student ID')),
                ('Country', models.CharField(default='india', max_length=200, verbose_name='Country(Lowercase)')),
                ('ProfilePicture', models.FileField(blank=True, default='covers/profile.png', upload_to='covers/', verbose_name='File')),
            ],
        ),
        migrations.DeleteModel(
            name='Design',
        ),
        migrations.DeleteModel(
            name='Nas',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='studnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
    ]
