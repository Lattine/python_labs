# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
from flask import Flask
from celery_app import celery
from config import config


def create_app(cfg_name):
    app = Flask(__name__)
    app.config.from_object(config[cfg_name])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .scheduled import scheduled as schehuled_blueprint
    app.register_blueprint(schehuled_blueprint)
    return app


def make_celery(app):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
