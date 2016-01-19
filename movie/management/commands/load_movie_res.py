# -*- coding:utf-8 -*-
import os
import ast
import jieba
from tqdm import tqdm
from django.conf import settings
from django.db import IntegrityError, transaction
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)
from django.core.management.base import BaseCommand, CommandError
from movie.models import Movie, MovieRes
from movie._global import SEP


jieba.load_userdict(settings.MOVIE_DICT)


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def get_movie(self, name):
        """
        尝试得到电影的真名
        """
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

    def handle(self, *args, **option_list):
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                lines = open(option_list['path'][0]).readlines()
                with transaction.atomic(), tqdm(total=len(lines)) as pbar:
                    for line in lines:
                        item = ast.literal_eval(line)
                        item['name'] = item['name'].strip()
                        item.pop('_type', None)
                        item.pop('_key', None)
                        try:
                            m = self.get_movie(item['name'])
                            MovieRes.objects.update_or_create(
                                movie=m,
                                name=item['name'],
                                defaults=item)
                        except ObjectDoesNotExist:
                            m = Movie.objects.create(name=item['name'])
                            MovieRes.objects.update_or_create(
                                movie=m,
                                defaults=item)
                        pbar.update()

            except (KeyError, IntegrityError,
                    FieldDoesNotExist, FieldError) as e:
                raise CommandError(e.message)
