# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 01:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_categories_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
    ]
