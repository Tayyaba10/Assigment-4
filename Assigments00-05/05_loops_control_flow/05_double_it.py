""" 
Write a program that asks a user to enter a number. 
Your program will then double that number and print 
out the result. It will repeat that process until 
the value is 100 or greater.
"""

def main():
    
    number = 100

    # ask the user input
    current_value = int(input("Enter a number: "))

    # double the number until the value is 100 or greater
    while current_value < number:
        current_value = current_value * 2
        print(current_value, end= " ")

if __name__ == '__main__':
    main()