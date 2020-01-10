from flask import Blueprint

demo = Blueprint("demo", __name__, url_prefix="/demo")

from . import views
