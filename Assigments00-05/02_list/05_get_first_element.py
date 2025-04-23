"""
Fill out the function get_first_element(lst) which 
takes in a list lst as a parameter and prints the first 
element in the list. The list is guaranteed to be non-empty. 
We've written some code for you which prompts the user to
input the list one element at a time.
"""

def get_first_element(lst):

    """ Prints the first element of a provided list. """
    print(lst[0])

def main():
    
    """ Prompts the user to enter one element of the list at a time and returns the resulting list."""

    num_element = int(input("How many elements in the list?"))
    lst = []

    for i in range(num_element):
        element = input(f"Enter an element in the list {i+ 1}:")
        lst.append(element)

    get_first_element(lst)


if __name__ == '__main__':
    main()