# backend/app/blueprints/recipe_ingredients.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import db, Recipe, Ingredient, RecipeIngredient

recipe_ingredients_blueprint = Blueprint('recipe_ingredients', __name__)


@recipe_ingredients_blueprint.route('/recipes/<int:recipe_id>/ingredients', methods=['GET'])
@jwt_required()
def get_recipe_ingredients(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    ingredients = [
        {
            'id': ri.ingredient_id,
            'name': ri.ingredient.name,
            'quantity': ri.quantity,
            'unit': ri.unit
        }
        for ri in recipe.recipe_ingredients
    ]
    return jsonify(ingredients), 200


@recipe_ingredients_blueprint.route('/recipes/<int:recipe_id>/ingredients', methods=['POST'])
@jwt_required()
def add_recipe_ingredient(recipe_id):
    data = request.get_json()
    ingredient_id = data.get('ingredient_id')
    quantity = data.get('quantity')
    unit = data.get('unit')

    recipe = Recipe.query.get_or_404(recipe_id)
    ingredient = Ingredient.query.get_or_404(ingredient_id)

    recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id, quantity=quantity, unit=unit)
    db.session.add(recipe_ingredient)
    db.session.commit()

    return jsonify({'message': 'Ingredient added to recipe'}), 201


@recipe_ingredients_blueprint.route('/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['PUT'])
@jwt_required()
def update_recipe_ingredient(recipe_id, ingredient_id):
    data = request.get_json()
    quantity = data.get('quantity')
    unit = data.get('unit')

    recipe_ingredient = RecipeIngredient.query.filter_by(recipe_id=recipe_id,
                                                         ingredient_id=ingredient_id).first_or_404()
    recipe_ingredient.quantity = quantity
    recipe_ingredient.unit = unit
    db.session.commit()

    return jsonify({'message': 'Ingredient updated'}), 200


@recipe_ingredients_blueprint.route('/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
@jwt_required()
def remove_recipe_ingredient(recipe_id, ingredient_id):
    recipe_ingredient = RecipeIngredient.query.filter_by(recipe_id=recipe_id,
                                                         ingredient_id=ingredient_id).first_or_404()
    db.session.delete(recipe_ingredient)
    db.session.commit()

    return jsonify({'message': 'Ingredient removed from recipe'}), 200
