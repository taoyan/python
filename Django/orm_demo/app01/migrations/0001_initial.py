# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-01 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('provice', models.CharField(max_length=32)),
                ('dept', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
