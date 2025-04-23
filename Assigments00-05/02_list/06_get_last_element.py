"""
Fill out the function get_last_element(lst) which takes
in a list lst as a parameter and prints the last element 
in the list. The list is guaranteed to be non-empty, but
there are no guarantees on its length.
"""

def get_last_element(lst):

    """print the last element in the list"""
    print(lst[-1])

def main():
    
    # input from the user
    num_element = int(input("How many elements in the list?"))

    lst = []

    for i in range(num_element):
        elements = input(f"Enter an element in the list {i + 1}:")
        lst.append(elements)

    get_last_element(lst)

if __name__ == '__main__':
    main()