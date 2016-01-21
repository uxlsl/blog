from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail

import requests


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
            for item in r.json():
                send_mail(item['title'], item['content'],
                          settings.EMAIL_HOST_USER, [item['email']],
                          fail_silently=False)
                self.stdout.write("send mail %s success" % item['email'])
                requests.patch(url, json={'id': item['id'], 'is_notify': True})

        except ValueError as e:
            pass
