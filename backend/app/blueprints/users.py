from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, db

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Email and password required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already registered"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered"}), 201


@users_blueprint.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200


@users_blueprint.route("/auth/login_telegram", methods=["POST"])
def login_telegram():
    data = request.get_json()
    telegram_id = data.get("telegram_id")

    if not telegram_id:
        return jsonify({"msg": "Telegram ID required"}), 400

    user = User.query.filter_by(telegram_id=telegram_id).first()

    if not user:
        return jsonify({"msg": "Invalid Telegram ID"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200


@users_blueprint.route("/auth/link_telegram", methods=["POST"])
@jwt_required()
def link_telegram():
    data = request.get_json()
    telegram_id = data.get("telegram_id")

    if not telegram_id:
        return jsonify({"msg": "Telegram ID required"}), 400

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    user.telegram_id = telegram_id
    db.session.commit()

    return jsonify({"msg": "Telegram account linked"}), 200


@users_blueprint.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    current_user_id = get_jwt_identity()

    if user_id != current_user_id:
        return jsonify({"msg": "Unauthorized"}), 401

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    user_data = {
        "id": user.id,
        "email": user.email,
        "telegram_id": user.telegram_id,
        "created_at": user.created_at
    }

    return jsonify(user_data), 200
