# conda create -n hw1 python=3.14
# conda activate hw1
# pip install "fastapi[standard]"
# pip install python-dotenv
# pip install psycopg2

import psycopg2
from config import DATABASE_URL

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows

    def commit(self):
        self.connection.commit()