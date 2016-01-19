# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from movie._utils import movie_res_update


class Command(BaseCommand):
    help = "获得最新电影资源数据并推送到服务器"

    def handle(self, *args, **option_list):
        for project, spider_name in settings.SPIDERS:
            movie_res_update(settings.API_KEY,
                             settings.CREATE_URL,
                             project,
                             spider_name
                             )
