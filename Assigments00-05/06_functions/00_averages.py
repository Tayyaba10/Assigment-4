""" Write a function that takes two numbers and finds the average between the two."""

# Function to find the average of two numbers
def average_number(a,b):
    """
    Returns the number which is half way between a and b
    """
    total = a + b
    return total / 2

def main():
    # ask the user input number
    a = float(input("Enter a first number: "))
    b = float(input("Enter a second number: "))
    # print the average number
    print("The average number is : ", average_number(a,b))

if __name__ == '__main__':
    main()