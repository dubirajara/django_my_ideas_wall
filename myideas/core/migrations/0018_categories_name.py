# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_categories_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
