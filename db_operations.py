import os
import sqlite3
import datetime
import json


db_filename = 'bid_ask.db'
schema_filename = 'bid_ask_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

    else:
        print('Database exists, assume schema does, too.')


class DbOperations():

    def insert(self, bid_ask_dict, source):
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            query = "insert into bid_ask (bid_ask_value, source, timestamp) values (:bid_ask_value, :source, :timestamp)"
            cursor.execute(query, {'bid_ask_value': str(bid_ask_dict), 'source': str(source), 'timestamp' : datetime.datetime.now()})
    
    def delete_old_data(self):
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("delete from bid_ask where timestamp < date('now','-5 days');")

    def delete_all(self):
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("delete from bid_ask")

    def get_last_bid_ask(self):
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            select * from bid_ask ORDER BY date(timestamp) DESC Limit 1
            """)
            row = cursor.fetchone()
            print(str(row[1]))
            return json.loads(str(row[1]).replace("'", '"'))