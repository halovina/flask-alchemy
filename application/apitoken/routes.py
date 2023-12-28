from .import apitoken_blueprint
from flask import jsonify, make_response, request
from application.internal.enkripsi import signature_auth

@apitoken_blueprint.route('/apitoken/signature-auth', methods=['POST'])
def signature_auth_token():
    xtimestamp = request.headers.get('X-TIMESTAMP')
    xclientkey = request.headers.get('X-CLIENT-KEY')
    string_tosign = "{}|{}".format(xclientkey, xtimestamp)
    privatekey = request.headers.get('PRIVATE-KEY')
    
    return make_response(
        jsonify({
            'signature': signature_auth(privatekey.replace(r'\n', '\n'), string_tosign)
        }), 200
    )