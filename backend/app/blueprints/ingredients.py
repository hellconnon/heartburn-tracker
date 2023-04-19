from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Ingredient, db

ingredients_blueprint = Blueprint('ingredients', __name__)


@ingredients_blueprint.route('/ingredients', methods=['GET'])
@jwt_required()
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify([ingredient.serialize() for ingredient in ingredients])


@ingredients_blueprint.route('/ingredients', methods=['POST'])
@jwt_required()
def add_ingredient():
    data = request.get_json()
    name = data.get('name')
    fats = data.get('fats')
    calories = data.get('calories')
    proteins = data.get('proteins')
    carbohydrates = data.get('carbohydrates')

    if not name:
        return jsonify({"message": "Ingredient name is required"}), 400

    ingredient = Ingredient(name=name, fats=fats, calories=calories, proteins=proteins, carbohydrates=carbohydrates)
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient added successfully", "ingredient": ingredient.serialize()}), 201


@ingredients_blueprint.route('/ingredients/<int:id>', methods=['PUT'])
@jwt_required()
def update_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({"message": "Ingredient not found"}), 404

    data = request.get_json()
    ingredient.name = data.get('name', ingredient.name)
    ingredient.fats = data.get('fats', ingredient.fats)
    ingredient.calories = data.get('calories', ingredient.calories)
    ingredient.proteins = data.get('proteins', ingredient.proteins)
    ingredient.carbohydrates = data.get('carbohydrates', ingredient.carbohydrates)

    db.session.commit()
    return jsonify({"message": "Ingredient updated successfully", "ingredient": ingredient.serialize()}), 200


@ingredients_blueprint.route('/ingredients/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({"message": "Ingredient not found"}), 404

    db.session.delete(ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient deleted successfully"}), 200
