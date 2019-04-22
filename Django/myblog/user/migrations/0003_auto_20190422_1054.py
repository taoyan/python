# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-22 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfo_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ('age',)},
        ),
        migrations.AddField(
            model_name='userinfo',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]