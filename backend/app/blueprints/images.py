# backend/app/blueprints/images.py

from flask import Blueprint, request, jsonify, send_from_directory, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os

from ..models import Image, db

images_blueprint = Blueprint("images", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@images_blueprint.route("/images", methods=["GET"])
@jwt_required()
def get_images():
    user_id = get_jwt_identity()
    images = Image.query.filter_by(user_id=user_id).all()
    return jsonify([image.to_dict() for image in images])


@images_blueprint.route("/images", methods=["POST"])
@jwt_required()
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    if file and allowed_file(file.filename):
        user_id = get_jwt_identity()
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.instance_path, "uploads", str(user_id), filename)
        # ensure file path exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        new_image = Image(user_id=user_id, file_name=filename)
        db.session.add(new_image)
        db.session.commit()
        return jsonify(new_image.to_dict()), 201
    else:
        return jsonify({"error": "Invalid file type"}), 400


@images_blueprint.route("/images/<int:image_id>", methods=["DELETE"])
@jwt_required()
def delete_image(image_id):
    user_id = get_jwt_identity()
    image = Image.query.filter_by(id=image_id, user_id=user_id).first()
    if image:
        os.remove(image.file_name)
        db.session.delete(image)
        db.session.commit()
        return jsonify({"message": "Image deleted"}), 200
    else:
        return jsonify({"error": "Image not found"}), 404


@images_blueprint.route("/images/<int:image_id>", methods=["GET"])
@jwt_required()
def get_uploaded_file(image_id):
    user_id = get_jwt_identity()
    file_name = Image.query.filter_by(id=image_id, user_id=user_id).first_or_404().file_name

    if file_name:
        user_directory = os.path.join(current_app.instance_path, "uploads", str(user_id))
        return send_from_directory(user_directory, file_name)
    else:
        return jsonify({"error": "Image not found"}), 404
