from functools import wraps
from flask import request, make_response, jsonify
import os
from marshmallow import ValidationError
from application.internal.pyjwt import jwtDecode
from datetime import datetime


def header_required(f):
    @wraps(f)
    def decorated_function(*args, **kwards):
        clientapikey = request.headers.get('client-api-key')
        if clientapikey != os.environ['CLIENT_APIKEY']:
            return make_response(
                jsonify({
                    'message':'Unauthorized header client-api-key'
                }), 401
            )
            
        bearer = request.headers.get('Authorization')
        bearer_token = bearer.split()
        if len(bearer_token) != 2:
            return make_response(
                jsonify({
                    'message':'Unauthorized header Authorization'
                }), 401
            )
        
        if bearer_token[0] != 'Bearer':
            return make_response(
                jsonify({
                    'message':'Unauthorized header Bearer'
                }), 401
            )
            
        decode_token = jwtDecode(bearer_token[1])
        if checkExpiredToken(decode_token['expired_time']) == False:
             return make_response(
                jsonify({
                    'message':'Unauthorized header Bearer token expired'
                }), 401
            )
            
        return f(*args, **kwards)
                
    return decorated_function


def checkExpiredToken(expired_time):
    current_time = datetime.now()
    current_unix_time = current_time.timestamp()
    
    if current_unix_time <= expired_time:
        return True
    
    return False


def required_param(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    'status':'errror',
                    'messages': err.messages
                }
                return make_response(
                    jsonify(error), 400
                )
            return f(*args, **kwargs)
        return wrapper
    return decorator