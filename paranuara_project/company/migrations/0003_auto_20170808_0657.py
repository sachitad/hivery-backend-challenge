# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170808_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='_id',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='guid',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
