# -*- coding:utf-8 -*-
from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import json
from django.db import models


class Movie(models.Model):
    name = models.CharField(unique=True, max_length=128, verbose_name="名称")
    url = models.URLField(verbose_name="所在网址")
    source = models.CharField(max_length=128, verbose_name="下载来源")
    down_urls = models.TextField(verbose_name="下载地址,多个数据json)")
    create_at = models.DateTimeField(auto_now=True,
                                     verbose_name="时间")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="更新时间")

    @property
    def download_urls(self):
        return json.loads(self.down_urls)
