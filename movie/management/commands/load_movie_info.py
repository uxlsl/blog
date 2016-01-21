# -*- coding:utf-8 -*-
import os
import json
import ast
from django.db import IntegrityError, transaction
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
    ObjectDoesNotExist
)
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **option_list):
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                f = open(option_list['path'][0])
                with transaction.atomic():
                    for item in f:
                        try:
                            item = ast.literal_eval(item)
                            del item['_type']
                            del item['_key']
                            if 'filmtype' not in item:
                                continue
                            item['filmtype'] = '|'.join(item['filmtype'])
                            item['name'] = '|'.join(item['name'])
                            Movie.objects.update_or_create(name=item['name'],
                                                           defaults=item)
                        except ObjectDoesNotExist:
                            pass
            except (KeyError, IntegrityError,
                    FieldDoesNotExist, FieldError) as e:
                raise CommandError(e.message)
