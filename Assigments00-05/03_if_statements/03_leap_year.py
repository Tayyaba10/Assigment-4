"""Write a program that reads a year from the user and tells whether a given year is a leap year or not."""

def main():

    # user input year
    year = int(input("Enter a year: "))

    #  year must be evenly divisible by 4
    if year % 4 == 0:
        # year must be evenly divisible by 100
        if year % 100 == 0:
            # year must be evenly divisible by 400
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            # not divisilble by 400
            else:
                print(f"{year} is a leap year.")
        # not divisilble by 100
        else:
            print(f"{year} is not a leap year.")
    # not divisilble by 4
    else:
        print(f"{year} is a leap year.")


if __name__ == '__main__':
    main()