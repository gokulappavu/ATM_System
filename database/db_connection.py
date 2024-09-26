import mysql.connector

class DatabaseConnection:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='@Vettriv357',
            database='atm_database'
        )

    def get_connection(self):
        return self.conn
