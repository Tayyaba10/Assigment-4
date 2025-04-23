"""
Ask the user for two numbers, one at a time, 
and then print the result of dividing the first 
number by the second and also the remainder of the division.
"""

def main():
    
    # Ask the user for two numbers
    dividend = int(input("\033[1;3m Please enter an integer to be divided:\033[0m"))

    divisor = int(input("\033[1;3m Please enter an integer to divide by:\033[0m"))

    # Calculate quotient and remainder
    qoutient = dividend // divisor

    remainder = dividend % divisor

    # Print the results
    print(f"The result of this division is {qoutient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()