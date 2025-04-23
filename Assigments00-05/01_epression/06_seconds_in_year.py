"""
Use Python to calculate the number of seconds in a year, a
nd tell the user what the result is in a nice print statement 
"""

#use constants
DAYS_PER_YEAR = 365
HOUR_IN_DAYS = 24
MINUTE_IN_HOUR = 60
SECOND_IN_MINUTE = 60

def main():

    #calculate the second in a year
    seconds_in_year = DAYS_PER_YEAR * HOUR_IN_DAYS * MINUTE_IN_HOUR * SECOND_IN_MINUTE

    #print the result 
    print(f"There are {seconds_in_year} seconds in a year!")


if __name__ == '__main__':
    main()