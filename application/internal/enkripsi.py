
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
from application.internal.configkey import publicKey

def signature_auth(privKey, stringToSign):
    digest = SHA256.new(bytes(stringToSign, 'utf-8'))
    private_key = RSA.importKey(privKey)
    
    signature_binary = PKCS1_v1_5.new(private_key).sign(digest)
    signature_binary_tobase64 = base64.b64encode(signature_binary).decode()
    return signature_binary_tobase64

def verified_signature_auth(signature, stringToSign):
    signatureDecodeB64 = base64.b64decode(signature)
    digest = SHA256.new(bytes(stringToSign, 'utf-8'))
    public_key = RSA.importKey(publicKey)
    verified = PKCS1_v1_5.new(public_key).verify(digest, signatureDecodeB64)
    return verified