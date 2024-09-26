class ExitOperation:

    def execute(self, atm_service):
        print('Thank you for using our ATM service!')
        print('Visit again!')
        atm_service.current_user = None 
