# -*- coding:utf-8 -*-
# https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_one/


from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from django.db import models
import jsonfield


class Movie(models.Model):
    """电影基本信息
    """
    name = models.CharField(unique=True, max_length=128, verbose_name="名称")
    url = models.URLField(blank=True, null=True, verbose_name="所在网址")
    filmtype = models.CharField(max_length=32, blank=True, null=True,
                                verbose_name="分类")
    filmscore = models.FloatField(default=0, verbose_name="评分")
    director = models.CharField(max_length=128, blank=True, null=True,
                                verbose_name="导演")
    starring = models.CharField(max_length=128,
                                blank=True,
                                null=True, verbose_name="主演")
    create_at = models.DateTimeField(auto_now=True,
                                     verbose_name="时间")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="更新时间")

    class Meta:
        verbose_name = "电影基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % (self.name)


class MovieRes(models.Model):
    """电影资源地址
    """
    PIAOHUA = 'piaohua'
    SOURCE_CHICES = (
        (PIAOHUA, '飘花电影网'),
    )
    movie = models.ForeignKey(Movie,
                              blank=True,
                              null=True)
    name = models.CharField(unique=True, max_length=128, verbose_name="名称")
    url = models.URLField(verbose_name="所在网址")
    source = models.CharField(max_length=128, choices=SOURCE_CHICES,
                              default=PIAOHUA,
                              verbose_name="下载来源")
    down_urls = jsonfield.JSONField()
    create_at = models.DateTimeField(auto_now=True,
                                     verbose_name="时间")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="更新时间")

    class Meta:
        verbose_name = "电影资源"
        verbose_name_plural = verbose_name
