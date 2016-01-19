# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_filmscore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': '电影基本信息', 'verbose_name': '电影基本信息'},
        ),
        migrations.AlterModelOptions(
            name='movieres',
            options={'verbose_name_plural': '电影资源', 'verbose_name': '电影资源'},
        ),
        migrations.AddField(
            model_name='movieres',
            name='name',
            field=models.CharField(max_length=128, verbose_name='名称', unique=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movieres',
            name='movie',
            field=models.ForeignKey(to='movie.Movie', null=True, blank=True),
        ),
    ]
