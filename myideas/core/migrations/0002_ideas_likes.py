# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='ideas_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]