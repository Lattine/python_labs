import os

BASE_URL = os.path.abspath(os.getcwd())


class Config:
    SECRET_KEY = os.environ.get("SECREET_KEY") or "1234567890"
    JSON_AS_ASCII = False  # 支持中文


config = {"default": Config}
