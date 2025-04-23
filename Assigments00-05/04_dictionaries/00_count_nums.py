""" This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information."""

# Dictionary to store number counts
number_counts = {}

def main():

    while True:
        enter_number = input("\x1b[1;34m Enter a number: ")

         # If the user enters a blank line, break out of the loop and stop asking for input
        if enter_number == "":
            break

        number = enter_number

        """ 
        Loop over the list of numbers. 
        If the number is not in the dictionary, add it as a key with a value of 1.
        If the number is in the dictionary, increment its value by 1.
        """
        if number in number_counts:
           number_counts[number] += 1
        else:
           number_counts[number] = 1

    # print the result
    for number, count in number_counts.items():
       print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()