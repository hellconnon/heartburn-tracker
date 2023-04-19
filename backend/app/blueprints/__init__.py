from flask import Flask
from .users import users_blueprint
from .symptoms import symptoms_blueprint
from .user_symptoms import user_symptoms_blueprint
from .recipes import recipes_blueprint
from .ingredients import ingredients_blueprint
from .images import images_blueprint
from .recipe_ingredients import recipe_ingredients_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(users_blueprint, url_prefix='/api')
    app.register_blueprint(symptoms_blueprint, url_prefix='/api')
    app.register_blueprint(user_symptoms_blueprint, url_prefix='/api')
    app.register_blueprint(recipes_blueprint, url_prefix='/api')
    app.register_blueprint(ingredients_blueprint, url_prefix='/api')
    app.register_blueprint(images_blueprint, url_prefix='/api')

