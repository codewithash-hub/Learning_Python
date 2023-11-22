import random

class Coin:
    def __init__(self) -> None:
        self.__sideup = random.randint(0, 1)

    def toss(self):

        if self.__sideup == 0:
            return "Heads"
        else:
            return "Tails"

    
my_coin = Coin()
print(my_coin.toss())

