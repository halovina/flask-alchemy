import os 
import jwt

def jwtEncode(payload):
    jwt_token = jwt.encode(payload, os.environ['SECRET_KEY'], algorithm="HS256")
    return jwt_token