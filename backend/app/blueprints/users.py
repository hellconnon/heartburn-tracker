from flask import Blueprint, request, jsonify
from flask_httpauth import HTTPBasicAuth
from backend.app.models import User
from backend.app.utils import authenticate_user, create_user, link_telegram_account

users_blueprint = Blueprint('users', __name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    user = authenticate_user(email, password)
    if user:
        return user


@users_blueprint.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = create_user(email, password)

    if user:
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'An error occurred during registration'}), 500


@users_blueprint.route('/auth/login', methods=['POST'])
@auth.login_required
def login():
    user = auth.current_user()
    return jsonify({'message': 'User logged in successfully', 'user_id': user.id}), 200


@users_blueprint.route('/auth/link_telegram', methods=['POST'])
@auth.login_required
def link_telegram():
    data = request.get_json()
    telegram_id = data.get('telegram_id')

    if not telegram_id:
        return jsonify({'error': 'Telegram ID is required'}), 400

    user = auth.current_user()
    success = link_telegram_account(user, telegram_id)

    if success:
        return jsonify({'message': 'Telegram account linked successfully'}), 200
    else:
        return jsonify({'error': 'An error occurred while linking the Telegram account'}), 500


@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
@auth.login_required
def get_user(user_id):
    user = auth.current_user()

    if user.id != user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    return jsonify({
        'id': user.id,
        'email': user.email,
        'telegram_id': user.telegram_id,
        'created_at': user.created_at.isoformat()
    }), 200
