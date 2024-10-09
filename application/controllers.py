from database.db import Event, Player
from . import database
from .token_jwt import create_jwt
from securiry.password_hash import hashed_function

def event_submit(data):
    event_name = data['event_name']
    date = data['date']
    location = data['location']
    new_event = Event(event_name, date, location)
    database.insert_event(new_event)



def events():
    return database.get_all_events()


def registration_submit(form):
    name = form['name']
    nickname = form['nickname']
    email = form['email']
    password = hashed_function.get_hashed_password(form['password']) #pass hashing
    player = Player(name, nickname, email, password)
    database.registration(player)


def login_form_submit(form):
    entity = database.get_player_by_credential(form['email'], hashed_function.get_hashed_password(form['password']))
    if entity:
        token = create_jwt(entity.player_id)
        return token
















