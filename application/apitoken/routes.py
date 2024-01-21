from .import apitoken_blueprint
from flask import jsonify, make_response, request
from application.internal.enkripsi import (signature_auth, verify_signature_auth, bearer_token,
                                           hmac_signature_service)

from .common import string_to_hex, json_to_minify


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
def verify_signature_auth_token():
    xtimestamp = request.headers.get('X-TIMESTAMP')
    xclientkey = request.headers.get('X-CLIENT-KEY')
    string_tosign = "{}|{}".format(xclientkey, xtimestamp)
    
    signature = request.headers.get('X-SIGNATURE')
    
    if verify_signature_auth(signature, string_tosign):
        return make_response(
            #generate bearer token
            
            jsonify({
                "responseMessage":"Successful",
                "accessToken": bearer_token(xclientkey, string_tosign),
                "tokenType":"Bearer",
                "expiresIn":"900",
                "additionalInfo":{}
                }), 200
        )
    
    return make_response(
        jsonify({
            "responseMessage":"Unatuhorized",
            }), 401
    )
    
    
@apitoken_blueprint.route('/apitoken/signature-service', methods=['POST'])
def hmac_sugnature_auth_service():
    xtimestamp = request.headers.get('X-TIMESTAMP')
    xsecretkey= request.headers.get('X-CLIENT-SECRET')
    accesstoken = request.headers.get('AccessToken')
    endpointurl = request.headers.get('EndpoinUrl')
    bodyReq = request.json
    
    print(request.base_url)
    
    secretKey = "{}|{}|{}".format(
        xsecretkey,
        xtimestamp,
        accesstoken
    )
    
    stringToSign = "{}:{}:{}:{}:{}:{}".format(
        "POST",
        endpointurl,
        accesstoken,
        string_to_hex(json_to_minify(bodyReq)),
        xtimestamp,
        xsecretkey
    )
    
    
    signature = hmac_signature_service(secret_key=secretKey, string_tosign=stringToSign)
    
    return make_response(
        jsonify({
            'signature': signature
        })
    )
    
