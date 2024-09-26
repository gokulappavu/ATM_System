from operations.transaction_operation import TransactionOperation

class DepositOperation(TransactionOperation):

    def execute(self, atm_service):
        amount = float(input('Enter the amount to deposit: '))
        atm_service.cursor.execute('UPDATE customers SET balance = balance + %s WHERE username = %s', 
                                    (amount, atm_service.current_user))
        atm_service.db_connection.commit()
        print(f'Successfully deposited ${amount:.2f}.')
