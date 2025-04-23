""" Guess My Number """
import random

def main():
    print("Welcom Guess Number Game!")
    # generate random number
    secret_number = random.randint(1,99)

    print("I am thinking of a number between 0 and 99...")
    # user guess
    guess = int(input("Enter a number: "))

    while guess != secret_number:
        # if condition is true if guess is less than secret number
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        # empty print for new guess
        print()     
        # new guess from user
        guess = int(input("Enter a new guess: "))
    
    print(f"Congrats! The number was: {secret_number}")


if __name__ == '__main__':
    main()