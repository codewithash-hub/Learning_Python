import random 

class Coin:
    def __init__(self):
        self.__sideup = "Heads"
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = 'Tails'
            
    
        return self.__sideup

my_coin = Coin()
    
# my_coin.toss()

print(f'This side is up: {my_coin.toss()}')