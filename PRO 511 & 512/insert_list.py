def main():
    names = ['James', "Kathryn", 'Bill']
    
    
    index = int(input('Enter the index: '))
    item = input('Enter the item: ')
    names.insert(index, item)
    
    print(names)
    print(names.index(item))
if __name__ == '__main__':
    main()