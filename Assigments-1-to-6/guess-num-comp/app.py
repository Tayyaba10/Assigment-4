# Guess the Number Game Python Project (computer)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess_count = 0

    print(f"Think of a number between 1 and {x}...")
    print("I will try to guess it!")
    print("Please respond with 'h' if my guess is too high, 'l' if too low, or 'c' if correct.")

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since they're equal

        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        
        guess_count += 1

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} in {guess_count} tries!")
        else:
            print("Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    max_number = 100  # You can change this to any range you want
    computer_guess(max_number)
