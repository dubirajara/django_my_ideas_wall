# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20161222_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='description',
            field=models.TextField(),
        ),
    ]