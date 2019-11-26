# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
from app import create_app, make_celery

app = create_app("default")
celery = make_celery(app)

if __name__ == '__main__':
    app.run()