# -*- coding:utf-8 -*-
import os
import json
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
            try:
                seg_list = list(jieba.cut(name))
                n1 = seg_list[0]
                o = Movie.objects.get(name__startswith=n1)
                if o.name == n1:
                    return o
                elif len(o.name) > len(n1):
                    if SEP.match(o.name[len(n1)]):
                        return o
                else:
                    raise ObjectDoesNotExist()

            except MultipleObjectsReturned:
                raise ObjectDoesNotExist()

    def handle(self, *args, **option_list):
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                data = json.load(open(option_list['path'][0]))
                with transaction.atomic(), tqdm(total=len(data)) as pbar:
                    for item in data:
                        item['name'] = item['name'].strip()
                        item.pop('_type', None)
                        try:
                            m = self.get_movie(item['name'])
                            MovieRes.objects.update_or_create(
                                movie=m,
                                name=item['name'],
                                defaults=item)
                        except ObjectDoesNotExist:
                            self.stdout.write(
                                "%s does not exist" % (item['name']))
                            m = Movie.objects.create(name=item['name'])
                            MovieRes.objects.update_or_create(
                                movie=m,
                                defaults=item)
                        pbar.update()

            except (KeyError, IntegrityError,
                    FieldDoesNotExist, FieldError) as e:
                raise CommandError(e.message)
