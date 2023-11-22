class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, bal):
        self.__balance += bal

        return self.__balance
    
    def withdraw(self, bal):

        if bal <= self.__balance:
            self.__balance -= bal
        else:
            self.__balance = "Insufficient funds"

        return f"You remaining balance is {self.__balance}"
    

money_in = float(input("Enter the amount you like to deposit: "))
money_out = float(input("Enter the amount you like to withdraw: "))

deposit = BankAccount()
print(deposit.deposit(money_in))
print(deposit.withdraw(money_out))