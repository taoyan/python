# Generated by Django 2.1.5 on 2019-03-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todos', '0007_auto_20190325_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='delete_status',
            field=models.IntegerField(default=0),
        ),
    ]
