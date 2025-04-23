"""
Sophia has a fruit store. She has written a 
function num_in_stock which takes a string fruit 
as a parameter and returns how many of that fruit 
are in her inventory. Write code in main() which will:
"""

# function to get the number of fruit in stock
def num_in_stock(fruit):
    # fruits in stock 
    inventry = {
        'apple' : 30,
        'orange': 50,
        'kiwi': 80,
        'pear': 0,
        'banana': 100,
        'grapes':60
    }

    return inventry.get(fruit.lower(), 0)

def main():
    # ask the user input
    fruit = input('\033[1;3m Enter a fruit: \033[0m ')

    count = num_in_stock(fruit)

    # if fruit not in stock then print
    if count == 0:
        print("This fruit is not in stock.")
    # if fruit in stock and then print 
    else:
        print("This fruit is in stock! Here is how many:")
        print(count)

if __name__ == '__main__':
    main()