# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-28 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190528_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='phone',
            new_name='mobile',
        ),
    ]
