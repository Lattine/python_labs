# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
import os

BASE_URL = os.path.abspath(os.getcwd())


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


class DevConfig(Config):
    debug = True


class ProConfig(Config):
    debug = False


config = {
    "dev": DevConfig,
    "pro": ProConfig,
    "default": DevConfig,
}
