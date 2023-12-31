class SavingsAccount:
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal
        
        
    def set_account_num(self, account_num):
        self.__account_num = account_num
        
    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate
        
    def set_balance(self, bal):
        self.__balance = bal
        
    def get_account_num(self):
        return self.__account_num
    
    def get_interest_rate(self):
        return self.__interest_rate
    
    def get_balance(self):
        return self.__balance
    
    
class CD(SavingsAccount):
    def __init__(self, account_num, int_rate, bal, maturity_date):
        SavingsAccount.__init__(self, account_num, int_rate, bal)
        self.__maturity_date = maturity_date
        
    def set_maturity_date(self, maturity_date):
        self.__maturity_date = maturity_date
            
    def get_maturity_date(self):
        return self.__maturity_date
    
    
            
        
        