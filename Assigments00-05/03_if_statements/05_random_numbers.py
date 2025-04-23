""" Print 10 random numbers in the range 1 to 100. """

# import random library
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():

    # for loop use and generate random number between minimium value and maximium value
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE , MAX_VALUE)
        print(value , end= " ")

if __name__ == '__main__':
    main()