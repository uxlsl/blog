# -*- coding:utf-8 -*-
import os
import ast
from tqdm import tqdm
from django.db import IntegrityError, transaction
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
)
from django.core.management.base import BaseCommand, CommandError
from movie.models import MovieRes


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **option_list):
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                lines = open(option_list['path'][0]).readlines()
                with transaction.atomic(), tqdm(total=len(lines)) as pbar:
                    for line in lines:
                        item = ast.literal_eval(line)
                        item['name'] = item['name'].strip()
                        MovieRes.create(item)
                        pbar.update()

            except (KeyError, IntegrityError,
                    FieldDoesNotExist, FieldError) as e:
                raise CommandError(e.message)
