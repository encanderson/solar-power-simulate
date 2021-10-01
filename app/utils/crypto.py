from cryptography.fernet import Fernet
from app.utils import mongo_manager
import json

key = Fernet.generate_key()

db = mongo_manager('manager')


def generate_key():
    key = Fernet.generate_key()
    coll = db["_KeyVault"]
    coll.insert_one({"kms": "orihome", "key": key})
    return True


def encrypt(data):
    coll = db["_KeyVault"]
    key = coll.find_one({"kms": "orihome"})
    if key:
        key = key["key"]
        cipher = json.dumps(data)
        encrypt = Fernet(key).encrypt(cipher.encode("utf-8"))
        return encrypt
    else:
        return None


def decrypt(data):
    coll = db["_KeyVault"]
    key = coll.find_one({"kms": "orihome"})
    if key:
        key = key["key"]
        if type(data) == bytes:
            decrypt = json.loads(Fernet(key).decrypt(data).decode())
        else:
            decrypt = Fernet(key).decrypt(data.encode("utf-8")).decode()
        return decrypt
    else:
        return None
