class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, bal):

        self.__balance += bal

        return self.__balance
    
    def withdraw(self, bal):

        if self.__balance >= bal:

            self.__balance -= bal
            return f"You remaining balance is {self.__balance}"
        else:
            return "Insufficient funds"
          

money_in = float(input("Enter the amount you like to deposit: "))
money_out = float(input("Enter the amount you like to withdraw: "))

my_account = BankAccount()
print(my_account.deposit(money_in))
print(my_account.withdraw(money_out))

# amount = 1

# def deposit(bal):
#     global amount

#     amount += bal
#     print(amount)

# deposit(1000)