# password Generator 

import random

# This program generates random passwords based on user input for length and number of passwords.
def password_generator():
    
    #  Define the character sets
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%&*()_=-+/'
    
    all_characters = lowercase + uppercase + numbers + symbols
    
    # Get user input for password length and number of passwords
    print("Welcome to the Password Generator!")
    print("This program generates random passwords for you.")
    
    number_of_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of the password: "))
    
    # Generate the passwords here
    print("\nGenerated Passwords Here:")
    
    # Loop to generate the specified number of passwords
    for pwd in range(number_of_passwords):
        password = ' '
        for i in range(password_length):
            password += random.choice(all_characters)
        print(password)
        
if __name__ == "__main__":   
    password_generator()