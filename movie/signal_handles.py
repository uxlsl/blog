"""
通过信号进行一些操作!
"""
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async

from django.conf import settings
from .models import MovieUpdate, MovieRes, MovieNotify

logger = logging.getLogger(__name__)


def movie_notify_handle(instance):
    """将可以通知的标记
    """
    for item in MovieNotify.objects.filter(is_notify=False,
                                           is_can_notify=False):
        if item.key in instance.name:
            item.title = "你关注的{}有新电影更新".format(item.key)
            item.content = "{}".format(instance.name)
            item.is_can_notify = True
            logger.debug('one can notify %s', item)
            item.save()


@receiver(post_save, sender=MovieUpdate)
def my_handler(sender, **kwargs):
    """信息不是哪么重要,删除一些,使更新记录数量保持在一定数量上!
    """
    if MovieUpdate.objects.count() > settings.MAX_MOVIEUPDATE:
        for i in MovieUpdate.objects.all().order_by(
                '-update_at')[settings.MAX_MOVIEUPDATE:]:
            i.delete()


@receiver(post_save, sender=MovieRes)
def movie_notify(sender, instance, **kwargs):
    """电影通知
    """
    async('movie.signal_handles.movie_notify_handle', instance)
