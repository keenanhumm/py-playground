import random

coin = ['heads', 'tails']


def coin_toss(flips=1):
    for i in range(flips):
        print(random.choice(coin))


coin_toss(1)
