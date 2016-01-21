# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20160120_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieNotify',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(verbose_name='电影关健字', max_length=32)),
                ('email', models.EmailField(verbose_name='要通知的邮件地址', max_length=254)),
                ('is_notify', models.BooleanField(verbose_name='是否已经通知', default=False)),
                ('is_can_notify', models.BooleanField(verbose_name='是否可以通知', default=False)),
                ('update_at', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '电影通知',
                'verbose_name_plural': '电影通知',
            },
        ),
        migrations.AlterModelOptions(
            name='movieupdate',
            options={'verbose_name': '电影更新时间', 'verbose_name_plural': '电影更新时间', 'ordering': ('-update_at',)},
        ),
    ]
