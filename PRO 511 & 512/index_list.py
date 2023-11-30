def main():
    food = ['Pizza', 'Burger', 'Chips']
    
    item = input('Which item should I change? ')
    
    try:
        item_index = food.index(item)
        print(item_index)
        new_item = input('Enter the new value: ')
        
        food[item_index] = new_item
        print(food)
    except ValueError:
        print('That item was not found in the list.')
        
if __name__ == '__main__':
    main()
    