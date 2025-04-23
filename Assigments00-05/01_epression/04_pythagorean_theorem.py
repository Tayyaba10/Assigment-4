"""
Write a program that asks the user for the lengths of the two 
perpendicular sides of a right triangle and outputs the length 
of the third side (the hypotenuse) using the Pythagorean theorem!
"""
# import math library 
import math

def main():
    print("Welcome to the Hypotenuse Calculator!")

    # Enter the length of two perpendicular side of a right triangle
    ab = float(input("\033[1;3m Enter the length of AB:\033[0m"))

    ac = float(input("\033[1;3m Enter the length of AC:\033[0m"))

    #calulate the hypotenuse usind the pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)
    # dispaly the length of the third side  
    print(f"The length of BC (the hypotenuse) is: {bc}")



if __name__ == '__main__':
    main()