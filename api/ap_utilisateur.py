#!/usr/bin/python3
from flask import Flask, request, jsonify
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)

# Simuler une base de données en mémoire
utilisateurs = {}

# Endpoint pour créer un nouvel utilisateur
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'email' not in data or 'prenom' not in data or 'nom_de_famille' not in data:
        return jsonify({'error': 'Données manquantes'}), 400
    
    email = data['email']
    if email in utilisateurs:
        return jsonify({'error': 'Email déjà utilisé'}), 409
    
    utilisateur = {
        'id': str(uuid4()),
        'email': email,
        'prenom': data['prenom'],
        'nom_de_famille': data['nom_de_famille'],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    utilisateurs[email] = utilisateur
    return jsonify(utilisateur), 201

# Endpoint pour récupérer la liste de tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(utilisateurs.values())), 200

# Endpoint pour récupérer les détails d'un utilisateur spécifique
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    for utilisateur in utilisateurs.values():
        if utilisateur['id'] == user_id:
            return jsonify(utilisateur), 200
    return jsonify({'error': 'Utilisateur non trouvé'}), 404

# Endpoint pour mettre à jour les informations d'un utilisateur
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for utilisateur in utilisateurs.values():
        if utilisateur['id'] == user_id:
            if 'email' in data:
                utilisateur['email'] = data['email']
            if 'prenom' in data:
                utilisateur['prenom'] = data['prenom']
            if 'nom_de_famille' in data:
                utilisateur['nom_de_famille'] = data['nom_de_famille']
            utilisateur['updated_at'] = datetime.now().isoformat()
            return jsonify(utilisateur), 200
    return jsonify({'error': 'Utilisateur non trouvé'}), 404

# Endpoint pour supprimer un utilisateur
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    for email, utilisateur in list(utilisateurs.items()):
        if utilisateur['id'] == user_id:
            del utilisateurs[email]
            return '', 204
    return jsonify({'error': 'Utilisateur non trouvé'}), 404

if __name__ == '__main__':
    app.run(debug=True)
