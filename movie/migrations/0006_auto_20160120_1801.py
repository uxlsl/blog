# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20160116_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('update_at', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
            ],
            options={
                'ordering': ('update_at',),
                'verbose_name': '电影更新时间',
            },
        ),
        migrations.AlterField(
            model_name='movieres',
            name='down_urls',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='movieres',
            name='source',
            field=models.CharField(default='piaohua', choices=[('piaohua', '飘花电影网')], verbose_name='下载来源', max_length=128),
        ),
    ]
