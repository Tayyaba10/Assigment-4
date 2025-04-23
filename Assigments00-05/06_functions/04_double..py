"""
Fill out the double(num) function to return the result 
of multiplying num by 2. We've written a main() function 
for you which asks the user for a number, calls your code 
for double(num) , and prints the result.
"""

def double(num):
    return num * 2

def main():
    number = input("\033[1;3m Enter a number: \033[0m")
    number_double = double(number)
    print(f"Double that is", number_double)


if __name__ == '__main__':
    main()