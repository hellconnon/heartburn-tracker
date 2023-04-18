from flask import Flask
from .users import users_blueprint
from .symptoms import symptoms_blueprint
from .user_symptoms import user_symptoms_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(users_blueprint, url_prefix='/api')
    app.register_blueprint(symptoms_blueprint, url_prefix='/api')
    app.register_blueprint(user_symptoms_blueprint, url_prefix='/api')
