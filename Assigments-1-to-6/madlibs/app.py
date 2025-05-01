# Mads Libs python project

print("Welcome to Mad Libs!")
print("Please enter the following information to create your Mad Libs story.")
print("You can enter 'exit' at any time to quit.")

# Get user input for the Mad Libs story
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter a third noun: ")
noun4 = input("Enter a fourth noun: ")

verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter a third verb: ")

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter a third adjective: ")

# Check if the user wants to exit
print("\nHere is your Mad Libs story:")
print(f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}.")
print(f"One day, the {noun1} met a {adjective2} {noun2} who wanted to {verb2}.")
print("They became the best of friends and lived happily ever after.")
print(f"But one day, a mysterious {adjective3} {noun3} appeared and challenged them to a {noun4} contest.")
print(f"Together, the {noun1} and the {noun2} used their skills to {verb3} and won the contest!")
print("Everyone in the forest celebrated their victory with a grand feast.")
print("\nThank you for playing Mad Libs!")
print("You can play again by running the program again.")
print("Goodbye!")

