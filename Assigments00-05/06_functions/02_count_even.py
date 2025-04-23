"""
Fill out the function count_even(lst) which
first populates a list by prompting the user 
for integers until they press enter (please use 
the prompt "Enter an integer or press enter to stop: "),
and then prints the number of even numbers in the list.
"""

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    # store the count even number 
    count = 0
    # loop through the number in list
    for num in lst:
        if num % 2 == 0:
            count += 1

    # Print out how many even numbers we counted above
    print("Even number:",count)

def main():
    # make an empty list for integers
    lst = []

    while True:
        # ask the user number input
        number = input("Enter an integer or press enter to stop: ")

        # while the user does not enter nothing
        if number == "":
            break
        else:
            nums = int(number)
            lst.append(nums)

    count_even(lst) 
    
if __name__ == '__main__':
    main()