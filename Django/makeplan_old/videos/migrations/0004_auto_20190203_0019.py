# Generated by Django 2.1.5 on 2019-02-02 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20190125_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='type',
        ),
        migrations.AddField(
            model_name='video',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]
