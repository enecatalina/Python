# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0002_auto_20171023_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='desc',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]