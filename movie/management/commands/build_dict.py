# -*- coding:utf-8 -*-
import os
import json
from django.conf import settings
from django.db import IntegrityError, transaction
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
    ObjectDoesNotExist
)
from django.core.management.base import BaseCommand, CommandError
from movie.models import Movie
from movie._global import SEP


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str)

    def handle(self, *args, **option_list):
        path = option_list['path'] if option_list[
            'path'] else settings.MOVIE_DICT
        if path:
            with open(path, 'w') as f:
                for name, in Movie.objects.values_list('name'):
                    for i in SEP.split(name):
                        f.write("%s\n" % i.strip())
            self.stdout.write("%s write success\n" % path)
