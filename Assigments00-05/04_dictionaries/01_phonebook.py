""" In this program we show an example of using dictionaries to keep track of information in a phonebook."""

# Dictionary to store phonebook entries
phonebook = {} 

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        # user input
        name = input("Enter a name to lookup: ")

        # if the user enter a balnk, break the loop
        if name == "":
            break

        # if user enter a name then check phonebook 
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(phonebook[name])

def main():
    print("Welcome to the phonebook!")

    while True:
          
          #  Ask the user for names to story in a phonebook (dictionary).
          name = input("Enter a Name: ")

         # if the user enter a blank, break the loop and stop the asking user
          if name == "":
               break
          
         # Ask the user for number to story in a phonebook (dictionary).
          number = int(input("Enter a Phone Number: "))

          phonebook[name] = number
    
    # print the phonebook enteries result
    print("PhoneBook Enteries!")
    for name , number in phonebook.items():
          print(f"{name} : {number}")
    
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()