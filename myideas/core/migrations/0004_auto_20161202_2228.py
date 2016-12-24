# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 22:28
from __future__ import unicode_literals

from django.db import migrations
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161202_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True, help_text='Enter a comma-separated tag string', max_count=5, to='core._Tagulous_Ideas_tags'),
        ),
    ]
