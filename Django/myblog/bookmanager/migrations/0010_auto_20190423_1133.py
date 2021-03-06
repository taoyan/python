# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-23 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0009_auto_20190422_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookmanager.AuthorDetail'),
        ),
    ]
