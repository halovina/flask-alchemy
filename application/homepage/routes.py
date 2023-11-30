
from flask import request, jsonify, make_response
from . import route_api_blueprint

@route_api_blueprint.route('/', methods=['GET'])
def homepage():
    return make_response(
        jsonify({
            'message':'hello world'
        }), 200
    )