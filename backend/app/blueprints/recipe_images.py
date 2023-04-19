from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import RecipeImage, Image, Recipe, db

recipe_images_blueprint = Blueprint("recipe_images", __name__)


@recipe_images_blueprint.route("/recipes/<int:recipe_id>/images", methods=["GET"])
@jwt_required()
def get_recipe_images(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"message": "Recipe not found"}), 404

    images = [img.serialize() for img in recipe.images]
    return jsonify(images), 200


@recipe_images_blueprint.route("/recipes/<int:recipe_id>/images", methods=["POST"])
@jwt_required()
def add_image_to_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"message": "Recipe not found"}), 404

    image_id = request.form.get("image_id")
    if not image_id:
        return jsonify({"message": "Image ID not provided"}), 400

    image = Image.query.get(image_id)
    if not image:
        return jsonify({"message": "Image not found"}), 404

    recipe_image = RecipeImage(recipe_id=recipe_id, image_id=image_id)
    db.session.add(recipe_image)
    db.session.commit()

    return jsonify({"message": "Image added to recipe"}), 201


@recipe_images_blueprint.route("/recipes/<int:recipe_id>/images/<int:image_id>", methods=["DELETE"])
@jwt_required()
def remove_image_from_recipe(recipe_id, image_id):
    recipe_image = RecipeImage.query.filter_by(recipe_id=recipe_id, image_id=image_id).first()
    if not recipe_image:
        return jsonify({"message": "Image not found in recipe"}), 404

    db.session.delete(recipe_image)
    db.session.commit()

    return jsonify({"message": "Image removed from recipe"}), 200
