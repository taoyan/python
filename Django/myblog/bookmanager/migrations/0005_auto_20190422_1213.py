# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-22 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0004_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookmanager.Publisher'),
        ),
    ]
