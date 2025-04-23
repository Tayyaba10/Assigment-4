"""
We've provided you with the ADULT_AGE variable which has the 
age a person is legally classified as an adult (in the United States). 
Fill out the is_adult(age) function, which returns True if the 
function takes an age that is greater than or equal to ADULT_AGE.
If the function takes an age less than ADULT_AGE, return False instead.
"""

# constant adult age
ADULT_AGE = 18

def is_adult(age):

    # if age eqaul or greater then adult age print true otherwise fasle print 
    if age >= ADULT_AGE:
        return True
    
    return False
    
def main():

    print("Entered age is an adult age or is not an adult age!")

    # ask the user age input number 
    age = int(input("\033[1;3m How old is this person?: \033[0m"))

    # print the result true or false
    print(is_adult(age))

if __name__ == '__main__':
    main()