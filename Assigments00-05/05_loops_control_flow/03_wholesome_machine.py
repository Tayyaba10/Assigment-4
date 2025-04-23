"""
Write a program which prompts the user to type an affirmation 
of your choice (we'll use "I am capable of doing anything I put
my mind to.") until they type it correctly. Sometimes, especially 
in the midst of such uncertain times, we just need to be reminded 
that we are resilient, capable, and strong; this little Python 
program may be able to help!
"""

# constant affirmation
AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():

    # initial prompt
    print(f" \x1b[1;34m Please type the following affirmation: {AFFIRMATION}")

    while True:
        # user input
        user_input = input()

        # if the user input 
        if user_input == AFFIRMATION:
            print("That's right! :")
            break

        # if the user input is not the affirmation 
        else:
            print("Hmmm That was not the affirmation.")
            # ask the user to type the affirmation again
            print(f"Please type the following affirmation: {AFFIRMATION}")

if __name__ == '__main__':
    main()