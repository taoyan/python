# Generated by Django 2.1.5 on 2019-02-28 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todos', '0003_auto_20190227_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='remind_date',
            field=models.DateTimeField(null=True),
        ),
    ]