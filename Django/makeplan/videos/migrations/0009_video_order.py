# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-03 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20191003_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='order',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]