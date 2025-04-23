"""Implement the following function which takes in 3 integers as parameters"""

def in_range(n, low, high):

    """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

    if n >= low and n <= high:
        return True
    
    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

def main():
    # print the result range
    print(in_range(11,1,10))
    print(in_range(8,1,10))
    print(in_range(10,1,10))
    print(in_range(9,1,10))
    print(in_range(0,1,10))

if __name__ == '__main__':
    main()