"""
Write a program which continuously asks the user to 
enter values which are added one by one into a list. 
When the user presses enter without typing anything, print the list.
"""

def main():

    # make an empty list
    lst = []

    while True:
        #input from user
        value = input("Enter a value: ")

        # If user presses enter without typing anything, exit loop
        if value == "":
            break

        # adding value
        lst.append(value)

    # print the result
    print("Here's the list: ", lst)

if __name__ == '__main__':
    main()