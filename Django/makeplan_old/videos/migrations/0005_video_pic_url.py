# Generated by Django 2.1.5 on 2019-02-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20190203_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='pic_url',
            field=models.CharField(default='http://pm4u2yzfu.bkt.clouddn.com/default', max_length=1000),
        ),
    ]
