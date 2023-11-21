def main():
    prod_nums = ['V475', 'F937', 'Q143', 'R688']
    
    search = input('Enter a product number: ')
    
    if search in prod_nums:
        print(f'{search} was found in the list.')
    else:
        print(f'{search} was not found in the list.')
        
if __name__ == '__main__':
    main()