# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_likes', '0002_auto_20171017_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to='book_likes.users'),
            preserve_default=False,
        ),
    ]
