# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20160121_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='movienotify',
            name='content',
            field=models.TextField(default='', verbose_name='邮件内容'),
        ),
        migrations.AddField(
            model_name='movienotify',
            name='title',
            field=models.CharField(default='', max_length=32, verbose_name='主题'),
        ),
    ]
