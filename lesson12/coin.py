import random


class Coin:

    def __init__(self):
        self.sideup = "Орёл"

    def toss(self):
        if random.randint(0, 1):
            self.sideup = "Орёл"
        else:
            self.sideup = "Решка"

    def get_sideup(self):
        return self.sideup


def main():
    my_coin = Coin()
    print(my_coin.get_sideup())

if __name__ == '__main__':
    main()
