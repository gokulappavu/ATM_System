from operations.balance_inquiry import BalanceInquiry
from operations.deposit_operation import DepositOperation
from operations.withdrawal_operation import WithdrawalOperation
from operations.exit_operation import ExitOperation 

class TransactionManager:

    def __init__(self):
        self.transactions = {
            1: BalanceInquiry(),
            2: DepositOperation(),
            3: WithdrawalOperation(),
            4: ExitOperation()  
        }

    def execute_transaction(self, atm_service):
        while True:
            transaction_type = int(input('''
1. Balance Inquiry
2. Deposit
3. Withdrawal
4. Exit
Select transaction type: '''))

            if transaction_type in self.transactions:
                self.transactions[transaction_type].execute(atm_service)
            else:
                print('Invalid option. Please select a valid transaction type.')
