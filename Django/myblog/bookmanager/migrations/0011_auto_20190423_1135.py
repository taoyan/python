# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-23 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0010_auto_20190423_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.AuthorDetail'),
        ),
    ]
