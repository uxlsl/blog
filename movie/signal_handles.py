"""
通过信号进行一些操作!
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from .models import MovieUpdate


@receiver(post_save, sender=MovieUpdate)
def my_handler(sender, **kwargs):
    """信息不是哪么重要,删除一些,使更新记录数量保持在一定数量上!
    """
    if MovieUpdate.objects.count() > settings.MAX_MOVIEUPDATE:
        for i in MovieUpdate.objects.all().order_by(
                '-update_at')[settings.MAX_MOVIEUPDATE:]:
            i.delete()
