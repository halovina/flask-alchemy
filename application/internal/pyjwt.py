import os 
import jwt

def jwtEncode(payload):
    jwt_token = jwt.encode(payload, os.environ['SECRET_KEY'], algorithm="HS256")
    return jwt_token

def jwtDecode(jwt_token):
    payload = jwt.decode(jwt_token, os.environ['SECRET_KEY'], algorithms="HS256")
    return payload