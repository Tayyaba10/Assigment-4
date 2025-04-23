# Write a program which asks the user what their favorite animal is
def main():
    print("Favourite Animal Program!")
    animal : str = input("\033[1;3m What's your favorite animal?\033[0m")
    print(f"My favorite animal is also {animal}!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()