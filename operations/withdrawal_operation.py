from operations.transaction_operation import TransactionOperation

class WithdrawalOperation(TransactionOperation):

    def execute(self, atm_service):
        amount = float(input('Enter the amount to withdraw: '))
        atm_service.cursor.execute('SELECT balance FROM customers WHERE username = %s', (atm_service.current_user,))
        balance = atm_service.cursor.fetchone()[0]
        
        if amount <= balance:
            atm_service.cursor.execute('UPDATE customers SET balance = balance - %s WHERE username = %s', 
                                        (amount, atm_service.current_user))
            atm_service.db_connection.commit()
            print(f'Successfully withdrew ${amount:.2f}.')
        else:
            print('Insufficient funds.')
