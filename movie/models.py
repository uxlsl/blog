# -*- coding:utf-8 -*-
# https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_one/


from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import json
from django.db import models


class Movie(models.Model):
    """电影基本信息
    """
    name = models.CharField(unique=True, max_length=128, verbose_name="名称")
    filmtype = models.CharField(max_length=32, blank=True, null=True,
                                verbose_name="分类")
    director = models.CharField(max_length=128, blank=True, null=True,
                                verbose_name="导演")
    starring = models.CharField(max_length=128,
                                blank=True,
                                null=True, verbose_name="主演")
    create_at = models.DateTimeField(auto_now=True,
                                     verbose_name="时间")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="更新时间")


class MovieRes(models.Model):
    """电影资源地址
    """
    movie = models.ForeignKey(Movie,
                              models.SET_NULL,
                              blank=True,
                              null=True)
    url = models.URLField(verbose_name="所在网址")
    source = models.CharField(max_length=128, verbose_name="下载来源")
    down_urls = models.TextField(verbose_name="下载地址,多个数据json)")
    create_at = models.DateTimeField(auto_now=True,
                                     verbose_name="时间")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="更新时间")

    def foo():
        doc = """Doc string"""

        def fget(self):
            return json.loads(self.down_urls)

        def fset(self, value):
            self.down_urls = json.dumps(value)

        def fdel(self):
            del self._down_urls
        return locals()

    download_urls = property(**foo())
