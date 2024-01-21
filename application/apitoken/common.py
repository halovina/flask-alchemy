import json
import hashlib
from application.userservice.decorators import checkExpiredToken
from functools import wraps
from flask import request, make_response, jsonify
from application.internal.pyjwt import jwtDecode
from application.internal.enkripsi import verify_hmac_signature_service

def json_to_minify(bodyReq):
    return json.dumps(bodyReq, separators=(',',':'))

def string_to_hex(msg):
    hash = hashlib.sha256(bytes(msg, 'utf-8'))
    return hash.hexdigest()

def validate_header_signature(endpointurl, authorizationToken, bodytoHex, xtimestamp, xsecretkey, signature):
    secretKey = "{}|{}|{}".format(
        xsecretkey,
        xtimestamp,
        authorizationToken
    )
    
    stringToSign = "{}:{}:{}:{}:{}:{}".format(
        "POST",
        endpointurl,
        authorizationToken,
        bodytoHex,
        xtimestamp,
        xsecretkey
    )
    
    return verify_hmac_signature_service(
        secret_key=secretKey,
        string_tosign=stringToSign,
        signature=signature
    )

def validate_signature_service(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        xtimestamp = request.headers.get('X-TIMESTAMP')
        xsecretkey= request.headers.get('X-CLIENT-SECRET')
        bearerToken = request.headers.get('Authorization') # Bearer token---
        bearerTokenToSplit = bearerToken.split()
        
        if len(bearerTokenToSplit) != 2:
            return make_response(
                jsonify({
                    'message': 'Unauthorized header authorization'
                }), 401
            )
            
        if bearerTokenToSplit[0] != 'Bearer':
            return make_response(
                jsonify({
                    'message': 'Unauthorized header Bearer'
                }), 401
            )
            
        decode_token = jwtDecode(bearerTokenToSplit[1])
        if checkExpiredToken(decode_token['expired_time']) == False:
            return make_response(
                jsonify({
                    'message': 'Unauthorized Bearer token expired'
                }), 401
            )
            
        endpoinurl = str(request.base_url).replace('http://127.0.0.1:5000','')
        bodyReq = request.json
        bodytoHex = string_to_hex(json_to_minify(bodyReq))
        xsignature = request.headers.get('X-SIGNATURE')
        
        if validate_header_signature(
            endpointurl=endpoinurl,
            authorizationToken=bearerTokenToSplit[1],
            bodytoHex=bodytoHex,
            xtimestamp=xtimestamp,
            xsecretkey=xsecretkey,
            signature=xsignature
        ) is False:
            return make_response(
                jsonify({
                    'message': 'Unauthorized signature'
                }), 401
            )
        
        print("okkkkkk: {}".format(endpoinurl))
        return f(*args, **kwargs)
    return decorated_function