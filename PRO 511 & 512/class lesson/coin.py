import random

class Coin:
    def __init__(self):
        self.sideup = 'Tails'

        def toss(self):
            if random.randint(0, 1) == 0:
                self.sideup = "Heads"
            else:
                self.sideup = "Tails"

        def get_sideup(self):
            return self.sideup
        

def main():

    my_coin = Coin()

    print('This side is up:', my_coin.sideup())

    print(my_coin.toss())

main()
