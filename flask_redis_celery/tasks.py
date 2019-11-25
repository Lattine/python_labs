# -*- coding: utf-8 -*-

# @Time    : 2019/11/25
# @Author  : Lattine

# ======================
from flask_mail import Message
from app import celery, mail


@celery.task
def send_mail(data):
    msg = Message("Ping Test!", sender="xxx@xxx.com", recipients=[data["email"]])
    msg.body = data["message"]
    mail.send(msg)
