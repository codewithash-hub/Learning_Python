import accounts

def main():
    acc_num = input('Enter your account number: ')
    int_rate = float(input('Enter your interest rate: '))
    balance = float(input('Enter your Balabce: '))

    savings = accounts.SavingsAccount(acc_num, int_rate, balance)
    
    acc_num = input('Enter your account number: ')
    int_rate = float(input('Enter your interest rate: '))
    balance = float(input('Enter your Balabce: '))
    maturinty = input('Maturity date: ')

    cd = accounts.SavingsAccount(acc_num, int_rate, balance, maturinty)
    
    # Display the data entered.
    print('Here is the data you entered:')
    print()
    print('Savings Account')
    print('---------------')
    print(f'Account number: {savings.get_account_num()}')
    print(f'Interest rate: {savings.get_interest_rate()}')
    print(f'Balance: R{savings.get_balance():,.2f}')

    print()
    print('CD')
    print('---------------')
    print(f'Account number: {cd.get_account_num()}')
    print(f'Interest rate: {cd.get_interest_rate()}')
    print(f'Balance: R{cd.get_balance():,.2f}')
    print(f'Maturity date: {cd.get_maturity_date()}')


if __name__ == '__main__':
    main()