import sqlite3

import db_scripts
from db_scripts import create_table


class Database:
    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, script):
        try:
            self.cursor.executescript(script)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f'error occurred{e}:')
            self.connection.rollback()
            return False

    def insert_one(self, data: dict):  # player name, nickname, event_name, day, location, link
        try:
            self.cursor.execute('INSERT INTO information (name, nickname, event_name, day, location, link) '
                                'VALUES (:name, :nickname, :event_name, :day, :location, :link)')
            self.connection.commit()
            data = self.cursor.lastrowid
            return data
        except sqlite3.Error as e:
            self.connection.rollback()
            return f'error occurred{e}'

    def fetch_one_id(self, id):
        try:
            self.cursor.execute('SELECT * WHERE id = ?', (id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            return f'error occurred{e}'



d = Database()
s = db_scripts.create_table
d.create_table(s)