# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-03 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_video_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='content',
            new_name='detail',
        ),
    ]
