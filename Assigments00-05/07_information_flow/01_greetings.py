"""
We've written a helper function for you called greet(name) 
which takes as input a string name and prints a greeting. 
Write some code in main() to get the user's name and then 
greet them, being sure to call the greet(name) helper function.
"""

def greet(user_name):
    return (f"Greeting {user_name}!")

def main():

    # user input string and print 
    user_name = str(input("\033[1;3m What's your name? \033[0m"))
    print(greet(user_name))

if __name__ == '__main__':
    main()