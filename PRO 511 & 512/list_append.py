def main():
    name_list = []
    
    again = 'y'
    while again.lower() == 'y':
        name = input('Enter a name: ')
        name_list.append(name)
        again = input('y for yes, anything else is no.')
    for name in name_list:
        print(name)
        
if __name__ == '__main__':
    main()