# -*- coding:utf-8 -*-
import os
import json
import jieba
from django.conf import settings
from django.db import IntegrityError, transaction
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
    ObjectDoesNotExist
)
from django.core.management.base import BaseCommand, CommandError
from movie.models import Movie, MovieRes


def get_movie(name):
    jieba.load_userdict(settings.MOVIE_DICT)
    seg_list = list(jieba.cut(name))
    print(seg_list)
    return Movie.objects.get(name=seg_list[0])


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **option_list):
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                data = json.load(open(option_list['path'][0]))
                with transaction.atomic():
                    for item in data:
                        try:
                            m = get_movie(item['name'])
                            MovieRes.objects.update_or_create(
                                movie=m,
                                name=item['name'])
                        except ObjectDoesNotExist:
                            self.stdout.write(
                                "%s does not exist" % (item['name']))
            except (KeyError, IntegrityError,
                    FieldDoesNotExist, FieldError) as e:
                raise CommandError(e.message)
