
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
from .configkey import publicKey
from datetime import datetime
from .pyjwt import jwtEncode
import hmac
import hashlib

def signature_auth(privKey, stringToSign):
    digest = SHA256.new(bytes(stringToSign, 'utf-8'))
    private_key = RSA.importKey(privKey)
    
    signature_binary = PKCS1_v1_5.new(private_key).sign(digest)
    signature_binary_tobase64 = base64.b64encode(signature_binary).decode()
    print("string to sign 1 {}".format(stringToSign))
    return signature_binary_tobase64

def verify_signature_auth(signature, stringToSign):
    signatureDecodeB64 = base64.b64decode(signature)
    digest = SHA256.new(bytes(stringToSign, 'utf-8'))
    public_key = RSA.importKey(publicKey)
    
    return PKCS1_v1_5.new(public_key).verify(digest, signatureDecodeB64) # true or false


def bearer_token(client_key, string_tosign):
    current_unix_time = datetime.now().timestamp()
    exprired_time = current_unix_time + 900
    return jwtEncode({
        'expired_time': exprired_time,
        'client_key': client_key,
        'string_tosign': string_tosign
    })
    

def hmac_signature_service(secret_key, string_tosign):
    hmac_digest = hmac.new(
        key=bytes(secret_key, 'utf-8'),
        msg=bytes(string_tosign, 'utf-8'),
        digestmod=hashlib.sha512
    ).digest()
    
    return base64.b64encode(hmac_digest).decode()


