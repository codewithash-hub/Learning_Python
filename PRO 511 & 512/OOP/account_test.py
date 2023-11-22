import bankaccount

def main():
    bank_acc = bankaccount.BankAccount
     
    start_bal = float(input('Enter your Starting balance: '))

    savings = bank_acc(start_bal)
    
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)
    
    
    print(f'Your account balance is R{savings.get_balance():,.2f}.')
    
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)
    
    print(f'Your account balance is R{savings.get_balance():,.2f}.') 


if __name__ == '__main__':
    main()    

    
    

