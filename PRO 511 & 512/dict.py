phonebook = {'Chris':'555-1111', 
             'Katie':'555-2222', 
             'Joanne':'555-3333'}

if 'chris' in phonebook:
    print(phonebook['Chris'])
else:
    print('Such key Error 404')
    
# Adding Elements to an Existing Dictionary

phonebook['Joe'] = '555-0123'
print(phonebook)

# Adding Elements to an Existing Dictionary 

if 'Chris' in phonebook:    
    del phonebook['Chris']
print(phonebook)

# Getting the Number of Elements in a Dictionary
num_items = len(phonebook)
print(num_items)