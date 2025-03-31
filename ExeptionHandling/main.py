amount = 1000

boolean = True

def withdraw(n):
    global amount
    if n <= amount:
        amount -= n
        print(amount)
    else:
        print("Not enough money.")
        print(f"The current amount is R{amount}")


while boolean:
    try:
        withdrawal = int(input("How much do yo want to withdraw (Press 000 to quit.): "))
        withdraw(withdrawal)
        if withdrawal == 000:
            boolean = False
    except ValueError:
        print("Invalid amount.")