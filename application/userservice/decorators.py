from functools import wraps
from flask import request, make_response, jsonify
import os


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