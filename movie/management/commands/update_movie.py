# -*- coding:utf-8 -*-
import os
import json
from django.core.management.base import BaseCommand, CommandError
from movie.models import Movie


class Command(BaseCommand):
    help = "更新电影资源数据"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **option_list):
        "更新"
        if (option_list['path']
                and os.path.isfile(option_list['path'][0])):
            try:
                data = json.load(open(option_list['path'][0]))
                for item in data:
                    del item['_type']
                    item['down_urls'] = json.dumps(item['down_urls'])
                    Movie.objects.update_or_create(name=item['name'],
                                                   defaults=item)
            except ValueError as e:
                raise CommandError(e.message)
