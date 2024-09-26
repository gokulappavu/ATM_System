from operations.transaction_operation import TransactionOperation

class BalanceInquiry(TransactionOperation):

    def execute(self, atm_service):
        """Executes the balance inquiry."""
        atm_service.cursor.execute('SELECT balance FROM customers WHERE username = %s', (atm_service.current_user,))
        balance = atm_service.cursor.fetchone()[0]
        print(f'Your current balance is: ${balance:.2f}')
