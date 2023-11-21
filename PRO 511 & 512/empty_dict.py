# Creating an Empty Dictionary
phonebook = {}



for i in range(5):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    phonebook[name] = phone_number
    
print(phonebook)