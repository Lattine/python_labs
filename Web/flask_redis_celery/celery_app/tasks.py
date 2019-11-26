# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
from . import celery
import time
import random


@celery.task(bind=True)
def celery_task(self):
    print("celery_app.task start")
    delay_time = random.randint(5, 20)
    time.sleep(delay_time)
    print("celery_app.task end.")
    return True
