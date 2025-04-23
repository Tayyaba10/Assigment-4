"""
Write a program which prompts the user for an adjective, then a noun, 
then a verb, and then prints a fun sentence
"""

# start constant sentence 
SENTENCE_CONST = "Code in Place is fun. I learned to program and used Python to make my"

def main():

    # get three input from user
    adjective = input("\033[1;3m Please type an adjective and press enter. \033[0m")

    noun = input("\033[1;3m Please type a noun and press enter.\033[0m")

    verb = input("\033[1;3m Please type a verb and press enter.\033[0m")

    # join the input together from sentence constant
    print(f"{SENTENCE_CONST} {adjective} {noun} {verb}!")


if __name__ == '__main__':
    main()