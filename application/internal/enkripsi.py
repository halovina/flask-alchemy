
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

def signature_auth(privKey, stringToSign):
    digest = SHA256.new(bytes(stringToSign, 'utf-8'))
    private_key = RSA.importKey(privKey)
    
    signature_binary = PKCS1_v1_5.new(private_key).sign(digest)
    signature_binary_tobase64 = base64.b64encode(signature_binary).decode()
    return signature_binary_tobase64