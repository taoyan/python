# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-31 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='start_date',
        ),
    ]
