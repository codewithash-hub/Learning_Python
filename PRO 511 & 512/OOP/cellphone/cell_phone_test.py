import cellphone

def main():

    man = input("Enter the phone's manufaccturer: ")
    mod = input("What is the model of the phone: ")
    price = float(input("Enter how much the phone cost: "))

    my_phone = cellphone.Cellphone(man, mod, price)
    
    print(f"The phone was designed by {my_phone.get_manu()}")
    print(f"The Model is {my_phone.get_model()}")
    print(f"Your {my_phone.get_model()} cost R{my_phone.get_price():,.2f}")


if __name__ == '__main__':
    main()