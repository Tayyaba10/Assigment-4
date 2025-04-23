""" 
Write a program that loops through a dictionary of fruits,
prompting the user to see how many of each fruit they want 
to buy, and then prints out the total combined cost of all of the fruits.
"""

def main():
    print("WELCOME to the fruit shop!)")

    # Dictionary with fruit names and prices
    fruit = {
        'apple':30,
        'orange': 40,
        'mango': 60,
        'kiwi': 50,
        'watermelon':30,
        'guava': 20,
    }

    total_cost = 0
    # for loop through a dictionary
    for fruits_names in fruit:
        price = fruit[fruits_names]
        #user input 
        amount_bought = int(input(f"\033[1;3m How many {fruits_names} do you want to buy?: \033[0m"))
        # total combine price of all of the fruit
        total_cost += (price * amount_bought)
    # print the result
    print(f"Your total is ${total_cost}")

if __name__ == '__main__':
    main()