"""
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
"""
def main():
    print("Calculate and print the perimeter of the triangle")
    # Get the 3 side lengths of the triangle
    side1 = float(input("\033[1;3m What is the length of side 1?\033[0m "))
    side2 = float(input("\033[1;3m What is the length of side 2? \033[0m "))
    side3 = float(input("\033[1;3m What is the length of side 3? \033[0m "))
    #add of the side of triangle
    perimeter = side1 + side2 + side3
    # Print out the perimeter (sum of the sides) of the triangle!
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()