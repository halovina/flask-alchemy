from functools import wraps
from flask import request, make_response, jsonify
import os
from marshmallow import ValidationError


def header_required(f):
    @wraps(f)
    def decorated_function(*args, **kwards):
        clientapikey = request.headers.get('client-api-key')
        if clientapikey == os.environ['CLIENT_APIKEY']:
            return f(*args, **kwards)
        else:
            return make_response(
                jsonify({
                    'message':'Unauthorized'
                }), 401
            )
                
    return decorated_function


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