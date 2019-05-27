# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-27 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('ident', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('content', models.TextField(null=True)),
                ('completeness', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('delete_status', models.IntegerField(default=0)),
                ('user_id', models.IntegerField()),
                ('last_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('ident', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=500)),
                ('group', models.IntegerField(default=0)),
                ('schedule_date', models.DateField()),
                ('finish_date', models.DateField(null=True)),
                ('remind_type', models.IntegerField(default=0)),
                ('remind_date', models.DateTimeField(null=True)),
                ('icon_index', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('user_id', models.IntegerField()),
                ('last_modified', models.DateTimeField()),
            ],
        ),
    ]
