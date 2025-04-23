"""
Converts feet to inches. Feet is an American unit of measurement. 
There are 12 inches per foot. Foot is the singular, 
and feet is the plural.
"""

#There are 12 inches for 1 foot
INCHES_IN_FOOT = 12

def main():
    feet = float(input("Enter number of feet:"))

    # perform the conversion
    inches = feet * INCHES_IN_FOOT

    # display the result in inches
    print(f"That is {inches} inches!")

if __name__ == '__main__':
    main()