from database.db import Event, Player
from . import database
from .token_jwt import create_jwt

def event_submit(data):
    event_name = data['event_name']
    date = data['date']
    location = data['location']
    new_event = Event(event_name, date, location)
    database.insert_one(new_event)


def player_submit(player_info):
    name = player_info['name']
    nickname = player_info['nickname']
    new_player = Player(name, nickname)
    database.insert_one(Player)



def events():
    return database.get_all_events()


def registration_submit(form):
    name = form['name']
    nickname = form['nickname']
    email = form['email']
    password = form['password']
    player = Player(name, nickname, email, password)
    database.registration(player)


def login_form_submit(form):
    entity = database.get_player_by_credential(form['email'], form['password'])
    if entity:
        token = create_jwt(entity.player_id)
        return token















