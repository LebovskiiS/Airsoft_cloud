import jwt
from confg import SECRET_KEY


def create_jwt(player_id):
    payload = {'id':player_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm= 'HS256')
    return token

def decode_jwt(token):
    try:
        if isinstance(token, str):  # Adding this check to convert string token to bytes
            token = token.encode('utf-8')
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.DecodeError) as e:
        return None