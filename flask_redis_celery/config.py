# -*- coding: utf-8 -*-

# @Time    : 2019/11/25
# @Author  : Lattine

# ======================
# ------------------- 项目配置 ----------------
SECRET_KEY = 'very_very_secure_and_secret'

# ------------------- Celery 配置 -----------------
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# -------------------- 邮件配置 ---------------------
MAIL_SERVER = "smtp.exmail.qq.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "liuzhi@iwowai.com"
MAIL_PASSWORD = "L6zhimakaimen"
