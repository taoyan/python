# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-02 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20191002_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]