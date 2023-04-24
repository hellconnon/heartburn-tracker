import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .blueprints import register_blueprints
from flask_jwt_extended import JWTManager
from .models import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # register blueprints
    register_blueprints(app)

    if test_config is None:
        # load config
        app.config.from_object('config.Config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # set up database
    db.init_app(app)

    # create database schema
    with app.app_context():
        db.create_all()

    # Enable JWT
    jwt = JWTManager(app)
    # Enable CORS for your frontend
    CORS(app, resources={r"/*": {"origins":"*"}})

    return app
