# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-04 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190702_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
