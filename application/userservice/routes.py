from ..models import User, Address
from flask import request, jsonify, make_response
from passlib.hash import sha256_crypt
from .. import db
from . import user_api_blueprint
from flask_login import login_user
from application.userservice.decorators import header_required, required_param
from application.userservice.user_schema import UserLoginSchema
import asyncio
from .utils import example_async_without_await


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
    
@user_api_blueprint.route('/api/user/login', methods=['POST'])
@required_param(UserLoginSchema())
def post_login():

    username = request.json['username']
    user =  User.query.filter_by(username=username).first()
    if user:
        if sha256_crypt.verify(str(request.json['password']), user.password):
            user.encode_api_key()
            db.session.commit()
            login_user(user)
            
            return make_response(
                jsonify({
                    'message':'logged in',
                    'api_key': user.api_key
                })
            )
    return make_response(
        jsonify({
            'message': 'not logged in'
        }), 401
    )
            
            
@user_api_blueprint.route('/api/user/all', methods=['GET'])
@header_required    
def get_all_user():
    users = User.query.all()
    data = []
    for x in users:
        xusers = {}
        xusers['user_id'] = x.id
        xusers['username'] = x.username
        xusers['first_name'] = x.first_name
        xusers['last_name'] = x.last_name
        xusers['email'] = x.email
        
        userAddress = Address.query.join(
            User, Address.user_id == User.id
        ).filter(Address.user_id == x.id).all()
        
        user_address = []
        for xaddress in userAddress:
            uad = {}
            uad['address'] = xaddress.address
            user_address.append(uad)
        
        xusers['user_address'] = user_address
        
        data.append(xusers)
   
    return make_response(
        jsonify({
            'message':'success',
            'data': data
        }), 200
    )
    
@user_api_blueprint.route('/api/user/test-async', methods=['GET'])
async def get_test_async_without_await():
    asyncio.create_task(example_async_without_await())
    return make_response(
        jsonify({
            'message':'OK'
        })
    )