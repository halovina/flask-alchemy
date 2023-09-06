from ..models import User
from flask import request, jsonify
from passlib.hash import sha256_crypt
from .. import db
from . import user_api_blueprint


@user_api_blueprint.route('/api/user/create', methods=['POST'])
def user_register():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    username = request.json['username']

    password = sha256_crypt.hash((str(request.json['password'])))

    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.username = username
    user.authenticated = True

    db.session.add(user)
    db.session.commit()
    
    return jsonify(
        {
            'message':'user added',
            'result': user.to_json()
        }
    )