# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views
