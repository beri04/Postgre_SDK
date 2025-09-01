import os 
from dotenv import load_dotenv
import psycopg2


load_dotenv()


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASS"),
            host = os.getenv("DB_HOST"),
            port = int(os.getenv("DB_PORT"))
        )
        self.cursor = self.conn.cursor()

    def execute_query(self,query,params = None):
        self.cursor.execute(query,params)
        self.conn.commit()
        return self.cursor.fetchall() if self.cursor.description else None
    
    def close(self):
        self.cursor.close()
        self.conn.close()