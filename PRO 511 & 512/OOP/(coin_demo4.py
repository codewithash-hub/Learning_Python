import coin

def main():
    my_coin = coin.Coin()
    
    my_coin.toss()
    
    print(f'This side is up: {my_coin.get_sideup()}')
    
    print('I am going to toss the coin ten times:')
    for i in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
    
if __name__ == '__main__':
    main()