import json
import hashlib

def json_to_minify(bodyReq):
    return json.dumps(bodyReq, separators=(',',':'))

def string_to_hex(msg):
    hash = hashlib.sha256(bytes(msg, 'utf-8'))
    return hash.hexdigest()