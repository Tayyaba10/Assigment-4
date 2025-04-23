"""
There are times where you are working with lots of different 
data within a function that you want to return. While generally,
we want to keep functions to have a precise purpose, sometimes 
that purpose just deals with multiple bits of data.
"""

def get_user_data():
    # ask the user input
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")

    return first_name , last_name, email_address

def main():
    # user data store and print 
    user_data = get_user_data()
    print("Received the following user data: ", user_data)

if __name__ == '__main__':
    main()