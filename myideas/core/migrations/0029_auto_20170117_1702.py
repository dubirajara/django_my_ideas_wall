# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20170106_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='slug',
            field=models.SlugField(max_length=60, null=True),
        ),
    ]
