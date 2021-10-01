from fastapi import HTTPException, Request
from pymongo import MongoClient
from app.config import settings
from dotenv import load_dotenv
from hashlib import sha256
import datetime
import jwt
import os

load_dotenv()

mongo_host = os.getenv('MONGO_HOST')


def mongo_manager(user):
    password = os.getenv(user.upper() + '_PASSWORD')
    uri = 'mongodb://{}:{}@{}:27017/?authMechanism=SCRAM-SHA-256'.format(
        user, password, mongo_host)
    db = MongoClient(uri)['manager']
    return db


def hashFunction(data):
    hashed = sha256(data.encode("UTF-8")).hexdigest()
    return hashed


async def generate_token(_id):
    token = jwt.encode({
        '_id': _id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
    }, settings.SECRET_KEY)

    return token.decode('utf-8')


def verify_token(token):
    try:
        print(token)
        current_user = jwt.decode(
            token, settings.SECRET_KEY)
        if current_user.get('_id'):
            return {
                'status': True,
                'message': "Usuário registrado com sucesso!"
            }
        else:
            return {
                'status': False,
                'message': 'Sessão inválida, por favor solicite outro convite!'
            }
    except Exception:
        return {
            'status': False,
            'message': 'Sessão inválida, por favor solicite outro convite!'
        }


async def token_required(request: Request):
    token = request.headers.get('Authorization')
    if token:
        token = token.split()[1]
        try:
            current_user = jwt.decode(
                token, settings.SECRET_KEY)
            return current_user.get('_id')
        except Exception:
            raise HTTPException(status_code=400, detail="Token inválido!")
    else:
        raise HTTPException(status_code=403, detail="Usuário não autorizado!")
