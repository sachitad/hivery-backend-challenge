# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('guid', models.CharField(max_length=40)),
                ('has_died', models.BooleanField(default=False)),
                ('picture_url', models.URLField()),
                ('age', models.IntegerField()),
                ('eye_color', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('registered', models.DateTimeField()),
                ('greeting', models.CharField(max_length=250)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='favorite_fruits',
            field=models.ManyToManyField(to='company.Fruit'),
        ),
        migrations.AddField(
            model_name='employee',
            name='favorite_vegetables',
            field=models.ManyToManyField(to='company.Vegetable'),
        ),
        migrations.AddField(
            model_name='employee',
            name='friends',
            field=models.ManyToManyField(to='company.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
