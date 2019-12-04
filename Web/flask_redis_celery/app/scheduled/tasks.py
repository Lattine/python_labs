# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
import time
from celery_app import celery


@celery.task
def scheduled_task(*args, **kwargs):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
