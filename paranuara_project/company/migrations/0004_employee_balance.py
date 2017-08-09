# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20170808_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
