# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-08 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190704_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
