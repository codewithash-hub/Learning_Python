NUM_DAYS = 5

def main():
    sales = [0] * NUM_DAYS
    print('Enter the sales for each day.')
    
    for index in range(len(sales)):
        sales[index] = float(input(f'Day #{index + 1}: '))
        
    print('Here are the values you entered:')
    for value in sales:
        print(value)
        
if __name__ == '__main__':
    main()