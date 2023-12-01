phonebook = {'Chris':'555-1111', 
             'Katie':'555-2222', 
             'Joanne':'555-3333'}

delete = phonebook.pop('Chris', 'Entry Not Found')
print(delete)

print(phonebook)