# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_employee_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('food_type', models.CharField(choices=[('F', 'Fruit'), ('V', 'Vegetable')], max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='favorite_fruits',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='favorite_vegetables',
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
        migrations.DeleteModel(
            name='Vegetable',
        ),
        migrations.AddField(
            model_name='employee',
            name='favorite_foods',
            field=models.ManyToManyField(to='company.Food'),
        ),
    ]
