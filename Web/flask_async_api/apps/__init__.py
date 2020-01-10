from flask import Flask
from flask_cors import CORS

from setting import config
from .demo import demo


def create_app(name="default"):
    app = Flask(__name__)
    app.config.from_object(config[name])
    app.register_blueprint(demo)

    CORS(app)
    return app
