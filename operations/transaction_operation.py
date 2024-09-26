from abc import ABC, abstractmethod

class TransactionOperation(ABC):

    @abstractmethod
    def execute(self, atm_service):
        pass
