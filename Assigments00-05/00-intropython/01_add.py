"""
This program asks the user for two
integers and prints their sum.
"""

def main():
    print("This is a basic arthmetic program is: Adds Two Numbers.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print(f"The sum of number is {total}.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()