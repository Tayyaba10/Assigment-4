"""
Fill out the subtract_seven helper function to subtract 
7 from num, and fill out the main() method to call the 
subtract_seven helper function! If you're stuck, revisit 
the add_five example from lecture.
"""

# helper function that substract from number
def subtract_seven(num):
    return num - 7
    
def main():
    # ask the user input
    number = int(input( "Enter anumber: "))
    result = subtract_seven(number)
    # print the result
    print("Resulting after substracting 7: ", result)

if __name__ == '__main__':
    main()