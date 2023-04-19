from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Recipe, RecipeIngredient, Ingredient, db

recipes_blueprint = Blueprint('recipes', __name__)


@recipes_blueprint.route('/recipes', methods=['GET'])
@jwt_required()
def get_all_recipes():
    user_id = get_jwt_identity()
    recipes = Recipe.query.filter_by(user_id=user_id).all()
    return jsonify([recipe.to_dict() for recipe in recipes])


@recipes_blueprint.route('/recipes', methods=['POST'])
@jwt_required()
def create_recipe():
    user_id = get_jwt_identity()
    data = request.get_json()

    recipe = Recipe(
        name=data['name'],
        type=data['type'],
        user_id=user_id
    )
    db.session.add(recipe)
    db.session.commit()

    return jsonify(recipe.to_dict()), 201


@recipes_blueprint.route('/recipes/<int:recipe_id>', methods=['GET'])
@jwt_required()
def get_recipe(recipe_id):
    user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first_or_404()

    return jsonify(recipe.to_dict())


@recipes_blueprint.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required()
def update_recipe(recipe_id):
    user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first_or_404()
    data = request.get_json()

    recipe.name = data['name']
    recipe.type = data['type']

    db.session.commit()
    return jsonify(recipe.to_dict())


@recipes_blueprint.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):
    user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first_or_404()

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'}), 200
