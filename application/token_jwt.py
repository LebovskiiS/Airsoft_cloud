import jwt
from confg import SECRET_KEY


def create_jwt(player_id):
    payload = {'id':player_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm= 'HS256')
    return token

def decode_jwt(token):
    data = jwt.decode(token, SECRET_KEY, algorithms= ['HS256'])
    return data