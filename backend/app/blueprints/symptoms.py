from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.models import Symptom, UserSymptom, db

symptoms_blueprint = Blueprint('symptoms', __name__)


@symptoms_blueprint.route('/symptoms', methods=['GET'])
@jwt_required()
def get_symptoms():
    symptoms = Symptom.query.all()
    return jsonify([symptom.to_dict() for symptom in symptoms]), 200


@symptoms_blueprint.route('/symptoms', methods=['POST'])
@jwt_required()
def add_symptom():
    data = request.get_json()

    name = data.get('name')
    if not name:
        return jsonify({"message": "Name is required."}), 400

    symptom = Symptom(name=name)
    db.session.add(symptom)
    db.session.commit()

    return jsonify(symptom.to_dict()), 201


@symptoms_blueprint.route('/symptoms/<int:symptom_id>', methods=['PUT'])
@jwt_required()
def update_symptom(symptom_id):
    data = request.get_json()
    symptom = Symptom.query.get_or_404(symptom_id)

    name = data.get('name')
    if not name:
        return jsonify({"message": "Name is required."}), 400

    symptom.name = name
    db.session.commit()

    return jsonify(symptom.to_dict()), 200


@symptoms_blueprint.route('/symptoms/<int:symptom_id>', methods=['DELETE'])
@jwt_required()
def delete_symptom(symptom_id):
    symptom = Symptom.query.get_or_404(symptom_id)
    db.session.delete(symptom)
    db.session.commit()
    return jsonify({"message": "Symptom deleted."}), 200
