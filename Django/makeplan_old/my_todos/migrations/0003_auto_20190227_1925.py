# Generated by Django 2.1.5 on 2019-02-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todos', '0002_auto_20190227_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finish_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='remind_date',
            field=models.DateField(null=True),
        ),
    ]
