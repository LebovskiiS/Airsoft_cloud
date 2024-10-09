import sqlite3
import confg
from .db_scripts import create_table_events, create_table_files, create_table_players
from securiry.password_hash import hashed_function

class Player:
    def __init__(self, name, nickname, email, password, player_id= None):
        self.player_id = player_id
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password





class Event:
    def __init__(self, event_name, date, location, event_id = None):
        self.event_id = event_id
        self.event_name = event_name
        self.date = date
        self.location = location


class File:
    def __init__(self, player_id, event_id, link,file_id= None):
        self.file_id = file_id
        self.link = link
        self.Player_id = player_id
        self.event_id = event_id




class Database:
    def __init__(self):
        self.connection = sqlite3.connect(confg.DATA_BASE_PATH, check_same_thread= False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(create_table_files)
        self.cursor.execute(create_table_events)
        self.cursor.execute(create_table_players)




    def insert_event(self, entity):
        self.cursor.execute('INSERT INTO events (event_name, date, location) VALUES (?,?,?) ',
                            [entity.event_name, entity.date, entity.location])
        self.connection.commit()
        entity.event_id = self.cursor.lastrowid
        return entity





    def get_all_events(self):
        data = self.cursor.execute('SELECT * FROM events')
        info = data.fetchall()
        entitis = []
        for i in info:
            ent = Event(i[1],i[2],i[3],i[0])
            entitis.append(ent)
        return entitis


    def registration(self, entity):
        self.cursor.execute('INSERT INTO players (name, nickname, '
                            'email, password)'
                            'VALUES (?,?,?,?)', [entity.name, entity.nickname, entity.email, entity.password])
        self.connection.commit()
        player_id = self.cursor.lastrowid
        entity.player_id = player_id
        return entity


    def get_player_by_credential(self, email, password):
        self.cursor.execute('SELECT * FROM players WHERE email = ? AND password = ?', [email, password])
        player_data = self.cursor.fetchone()
        if player_data is not None:
            player = Player(player_data[1], player_data[2], player_data[3], player_data[4], player_id= player_data[0])
            return player











