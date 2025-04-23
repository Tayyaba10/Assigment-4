"""
Fill out the function shorten(lst) which removes elements 
from the end of lst, which is a list, and prints each item 
it removes until lst is MAX_LENGTH items long. If lst is already 
shorter than MAX_LENGTH you should leave it unchanged. We've 
written a main() function for you which gets a list and passes 
it into your function once you run the program. For the autograder 
to pass you will need MAX_LENGTH to be 3, but feel free to change 
it around to test your program.
"""

MAX_LENGTH: int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        # remove list print
        print("Remove Items:",last_element)

def main():

    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    item = []

    while True:
        # input from user
        num_element = input(f"Enter an element in the list:")

        if num_element == "":
            break

        item.append(num_element)
    # call the function/*=
    shorten(item)

    # print the final list after remove item
    print("Shorten List:" , item)

if __name__ == '__main__':
    main()