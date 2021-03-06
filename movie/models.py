# -*- coding:utf-8 -*-
# https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_one/


from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from django.db import models
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)
import jsonfield
import jieba
from ._global import SEP
from django.conf import settings

is_load_userdict = False


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

    @staticmethod
    def get_movie(name):
        """
        尝试得到电影的真名
        """
        global is_load_userdict
        if not is_load_userdict:
            jieba.load_userdict(settings.MOVIE_DICT)
            is_load_userdict = True
        try:
            o = Movie.objects.get(name=name)
            return o
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            for n in jieba.cut(name):
                try:
                    o = Movie.objects.get(name__contains=n)
                    if n in SEP.split(o.name):
                        return o
                except MultipleObjectsReturned:
                    raise ObjectDoesNotExist()


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

    @staticmethod
    def create(data):
        data['name'] = data['name'].strip()
        data.pop('_type', None)
        data.pop('_key', None)
        try:
            m = Movie.get_movie(data['name'])
            return MovieRes.objects.update_or_create(
                movie=m,
                name=data['name'],
                defaults=data)[0]
        except ObjectDoesNotExist:
            m = Movie.objects.create(name=data['name'])
            return MovieRes.objects.update_or_create(
                movie=m,
                defaults=data)[0]


class MovieUpdate(models.Model):
    """电影资源每次更新的记录
    """
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "电影更新时间"
        verbose_name_plural = verbose_name
        ordering = ('-update_at', )


class MovieNotify(models.Model):
    """电影通知
    """
    key = models.CharField(max_length=32, verbose_name="电影关健字")
    email = models.EmailField(verbose_name="要通知的邮件地址")
    title = models.CharField(default='', max_length=32, verbose_name="主题")
    content = models.TextField(default='', verbose_name="邮件内容")
    is_notify = models.BooleanField(default=False, verbose_name="是否已经通知")
    is_can_notify = models.BooleanField(default=False, verbose_name="是否可以通知")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "电影通知"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{},{},{}'.format(self.key, self.email, self.title)
