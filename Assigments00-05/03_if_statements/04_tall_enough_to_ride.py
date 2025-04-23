"""Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height."""

# the minimum height is 50
MINIMIUM_HEIGHT : int= 50

def main():
    while True:
        # user input height
        height = input("\033[1;3m How tall are you? \033[0m ")

        # if height empty press stop this program
        if height == "":
            print("Goodbye! Have a great day!")
            break

        height = int(height)

        # check height condition and print message
        if height >= MINIMIUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

    
if __name__ == '__main__':
    main()