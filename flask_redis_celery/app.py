# -*- coding: utf-8 -*-

# @Time    : 2019/11/25
# @Author  : Lattine

# ======================
from __future__ import absolute_import
from flask import Flask
from flask_mail import Mail
from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


# -------------- 构造 Flask App --------------
def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    app.secret_key = app.config['SECRET_KEY']

    register_celery(app)
    return app


# -------------- 注册Celery到App --------------
def register_celery(app):
    celery.config_from_object('config')  # 读取配置文件

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


celery = Celery(__name__, backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND)
app = create_app()
mail = Mail(app)
