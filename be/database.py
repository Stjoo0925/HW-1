import psycopg2
from config import DATABASE_URL

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        if query.strip().upper().startswith("SELECT") or "RETURNING" in query.upper():
            rows = self.cursor.fetchall()
            return rows
        return []
        
    def commit(self):
        self.connection.commit()
