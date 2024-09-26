import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

    def get_connection(self):
        return self.conn
