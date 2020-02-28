from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
# db = SQLAlchemy()
from .db import MongoDB


def create_app(config_name):
    db = MongoDB()
    config_name = 'dev' if not config_name else config_name
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        # render home template
        return 'Hello, World!'

    return app
