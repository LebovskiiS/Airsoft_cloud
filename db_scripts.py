create_table = '''
CREATE TABLE IF NOT EXISTS information (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    nickname TEXT,
    event_name TEXT,
    day INTEGER,
    location TEXT,
    link TEXT NOT NULL
)
'''
