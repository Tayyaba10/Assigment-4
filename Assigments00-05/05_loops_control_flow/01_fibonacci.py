""" 
Write a program that displays the terms in the Fibonacci 
sequence, starting with Fib(0) and continuing as long as the 
terms are less than 10,000 (you should store this value as a constant!).
"""
# constant the maximiuim value
MAX_VALUE = 10000

def main():

    # starting value
    a, b = 0 , 1

    #  # Print Fibonacci numbers
    while a < MAX_VALUE:
        print(a, end = " ")
        a, b = b, a + b

if __name__ == '__main__':
    main()