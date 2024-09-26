from atm.atm_service import ATMService
from atm.transaction_manager import TransactionManager

if __name__ == "__main__":
    transaction_manager = TransactionManager()
    atm_service = ATMService(transaction_manager)
    atm_service.start_service()
