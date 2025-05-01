# Number guessing game 

import random

def guess_number():

    number_to_guess = random.randint(1, 50)
    attempts = 0
    max_attempts = 5

    print("\033[1;3m Welcome to the Number Guessing Game! \033[0m ")
    print("You have to do selected a number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess the number.")
    print("\033[3;3m Let's start! \033[0m")

    # Loop until the user guesses the number or runs out of attempts
    while attempts < max_attempts:
        # Get user input
        guess = int(input("Enter your guess number: "))
        attempts += 1

        # if guess less than number_to_guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        # greater then guess 
        elif guess > number_to_guess:
            print("Too high! Try again.")
        # correct answer  
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()