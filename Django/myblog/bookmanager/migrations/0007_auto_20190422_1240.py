# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-22 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0006_auto_20190422_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='bookmanager.Book'),
        ),
    ]