from operations.balance_inquiry import BalanceInquiry
from operations.deposit_operation import DepositOperation
from operations.withdrawal_operation import WithdrawalOperation

class TransactionManager:

    def __init__(self):
        self.transactions = {
            1: BalanceInquiry(),
            2: DepositOperation(),
            3: WithdrawalOperation()
        }

    def execute_transaction(self, atm_service):
        """Allows the user to select and execute a transaction."""
        while True:
            transaction_type = int(input('''
1. Balance Inquiry
2. Deposit
3. Withdrawal
4. Exit
Select transaction type: '''))

            if transaction_type in self.transactions:
                self.transactions[transaction_type].execute(atm_service)
            elif transaction_type == 4:
                print('Thank you for using our ATM service!')
                atm_service.current_user = None
                break
            else:
                print('Invalid option. Please select a valid transaction type.')