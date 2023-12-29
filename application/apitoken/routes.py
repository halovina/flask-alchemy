from .import apitoken_blueprint
from flask import jsonify, make_response, request
from application.internal.enkripsi import signature_auth, verified_signature_auth

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
    
@apitoken_blueprint.route('/apitoken/access-token-b2b', methods=['POST'])
def access_token_b2b():
    xtimestamp = request.headers.get('X-TIMESTAMP')
    xclientkey = request.headers.get('X-CLIENT-KEY')
    string_tosign = "{}|{}".format(xclientkey, xtimestamp)
    signature = request.headers.get('X-SIGNATURE')
    
    verified_signature = verified_signature_auth(string_tosign, signature)
    
    if verified_signature:
        return make_response(
            jsonify({
                "responseMessage":"Successful",
                "accessToken":"eyJhbGciOiJI",
                "tokenType":"Bearer",
                "expiresIn":"900",
                "additionalInfo":{}
            }), 200
        )
    
    return make_response(
        jsonify({
            "responseMessage":"Unauthorized",
        }), 401
    )
    
    