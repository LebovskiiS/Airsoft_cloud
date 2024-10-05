create_table_players = '''
CREATE TABLE IF NOT EXISTS players (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    nickname TEXT NOT NULL UNIQUE,  email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, cookies TEXT DEFAULT NULL
)
'''


create_table_events = '''
CREATE TABLE IF NOT EXISTS events
(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
event_name TEXT NOT NULL, date TEXT, location TEXT
)'''


create_table_files = '''
CREATE TABLE IF NOT EXISTS img
(ID INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT NOT NULL, 
user_id INTEGER REFERENCES users(ID), event_id INTEGER REFERENCES events(ID))
'''