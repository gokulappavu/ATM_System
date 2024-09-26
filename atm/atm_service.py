from database.db_connection import DatabaseConnection
from atm.transaction_manager import TransactionManager

class ATMService:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager
        self.db_connection = DatabaseConnection().get_connection()
        self.cursor = self.db_connection.cursor()
        self.current_user = None  

    def authenticate_user(self, username, pin):
        username = username.lower().strip()  
        self.cursor.execute('SELECT username, pin FROM customers WHERE LOWER(username) = %s', (username,))
        result = self.cursor.fetchone()

        if result and result[1] == pin:
            stored_username = result[0]  
            print(f'Welcome, {stored_username}!')
            self.current_user = stored_username  
            return True
        else:
            print('Invalid credentials.')
            return False

    def start_service(self):
        while True:
            username = input('Enter your username: ')
            pin = int(input('Enter your PIN: '))

            if self.authenticate_user(username, pin):
                transaction_manager = TransactionManager()
                transaction_manager.execute_transaction(self)
            else:
                print('Please try again..')