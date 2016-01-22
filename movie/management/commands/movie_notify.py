import logging
import traceback
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.mail import send_mail

import requests

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "发送电影更新信息到相关的用户"

    def add_arguments(self, parser):
        parser.add_argument('--client', action='store_true',
                            default=False,
                            help='是否是客户机')

    def handle(self, *args, **options):
        try:
            params = {'is_can_notify': True}
            url = settings.HOST + '/movie/movie_notify/'
            r = requests.get(url, params=params)
            logger.debug("url %s data %s", url, r.json())
            for item in r.json():
                send_mail(item['title'], item['content'],
                          settings.EMAIL_HOST_USER, [item['email']],
                          fail_silently=False)
                logger.info("send mail to %s success, title %s", item['email'],
                            item['title'])
                requests.patch(url, json={'id': item['id'], 'is_notify': True})

        except ValueError:
            logger.error('fail %s', traceback.format_exc())
