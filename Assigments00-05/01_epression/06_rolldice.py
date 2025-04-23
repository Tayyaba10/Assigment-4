""" 
Simulate rolling two dice, and prints results 
of each roll as well as the total.
"""
# import random library
import random

## Number of sides on each die to roll
NUM_SIDES = 6

def main():

    #roll die
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # total die of two
    total = die1 + die2

    #print the result
    print(f"Dice have, {NUM_SIDES} sides each.")

    print(f"First die: {die1}")

    print(f"Second die: {die2}")

    print(f"Total of two dice: {total}")


if __name__ == '__main__':
    main()