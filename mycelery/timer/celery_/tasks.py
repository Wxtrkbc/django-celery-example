from __future__ import absolute_import
from celery import shared_task


@shared_task()
def ping_net_task():
    print("ping_net_task")
