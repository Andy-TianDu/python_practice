__author__ = 'tian.du'

import random


def die_roll():
    i = random.randint(1, 6)
    print(i)
    # a deck of cards
    cards = ["jack", "queen", "king", "ace"]
    print(random.choice(cards))


def try_rolling():
    for i in (1, 2, 3):
        die_roll()
        i += 1


if __name__ == "__main__":
    try_rolling()
