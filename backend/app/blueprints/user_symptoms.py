from flask import Blueprint, request, jsonify
from ..models import User, UserSymptom, Symptom, db
from flask_jwt_extended import jwt_required, get_jwt_identity

user_symptoms_blueprint = Blueprint('user_symptoms', __name__)


# Get user's symptom logs
@user_symptoms_blueprint.route('/users/<int:user_id>/symptoms', methods=['GET'])
@jwt_required()
def get_user_symptoms(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({"message": "Unauthorized access"}), 401

    user_symptoms = UserSymptom.query.filter_by(user_id=user_id).all()
    return jsonify([symptom.to_dict() for symptom in user_symptoms]), 200


# Log a symptom for the user
@user_symptoms_blueprint.route('/users/<int:user_id>/symptoms', methods=['POST'])
@jwt_required()
def add_user_symptom(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({"message": "Unauthorized access"}), 401

    data = request.get_json()
    symptom_id = data.get('symptom_id')
    severity = data.get('severity')
    notes = data.get('notes')

    symptom = Symptom.query.get(symptom_id)
    if not symptom:
        return jsonify({"message": "Symptom not found"}), 404

    user_symptom = UserSymptom(user_id=user_id, symptom_id=symptom_id, severity=severity,
                               notes=notes)
    db.session.add(user_symptom)
    db.session.commit()

    return jsonify(user_symptom.to_dict()), 201


# Update a user's symptom log
@user_symptoms_blueprint.route('/users/<int:user_id>/symptoms/<int:symptom_log_id>', methods=['PUT'])
@jwt_required()
def update_user_symptom(user_id, symptom_log_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({"message": "Unauthorized access"}), 401

    user_symptom = UserSymptom.query.get(symptom_log_id)
    if not user_symptom:
        return jsonify({"message": "Symptom log not found"}), 404

    data = request.get_json()
    user_symptom.severity = data.get('severity', user_symptom.severity)
    user_symptom.notes = data.get('notes', user_symptom.notes)

    db.session.commit()
    return jsonify(user_symptom.to_dict()), 200


# Delete a user's symptom log
@user_symptoms_blueprint.route('/users/<int:user_id>/symptoms/<int:symptom_log_id>', methods=['DELETE'])
@jwt_required()
def delete_user_symptom(user_id, symptom_log_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({"message": "Unauthorized access"}), 401

    user_symptom = UserSymptom.query.get(symptom_log_id)
    if not user_symptom:
        return jsonify({"message": "Symptom log not found"}), 404

    db.session.delete(user_symptom)
    db.session.commit()

    return jsonify({"message": "Symptom log deleted successfully"}), 200
