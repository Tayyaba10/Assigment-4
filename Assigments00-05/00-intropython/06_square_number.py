# Ask the user for a number and print its square (the product of the number times itself).
def main():
    num = float(input("\033[1;3m Type a number to see its square: \033[0m"))

    square = num * num
    
    print(f"{num} squared is {square}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()