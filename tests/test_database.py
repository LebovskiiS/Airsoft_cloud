import unittest
import sqlite3
from database.db import Database
from database.db_scripts import create_table_events

data = {
            'name': 'John',
            'nickname': 'jd',
            'event_name': 'Music Fest',
            'day': '2023-02-25',
            'location': 'NY',
            'link': 'http://example.com'
}


class UnittestDatabase(unittest.TestCase):
    def setUp(self):
        self.Database = Database()
        self.Database.connection = sqlite3.connect(':memory:')
        self.Database.cursor = self.Database.connection.cursor()
        self.Database.create_table(create_table_events)
        self.Database.insert_one(data)


    def test_insert_one(self):
        result = self.Database.insert_one(data)
        self.assertIsInstance(result, dict)
        self.assertIn('user_id', result)
        self.assertIn('event_id', result)
        self.assertIn('file_id', result)


    def tearDown(self):
        self.Database.connection.close()


if __name__ == '__main__':
    unittest.main()

