"""
Write a program which asks a user for their age and
lets them know if they can or can't vote in the 
following three fictional countries.
"""

# voting age in different countries
Peturksbouipo :int  = 16
Stanlau :int = 25
Mayengua :int = 48

def main():

    # user's age input 
    user_age = int(input("\033[1;3m How old are you ?\033[0m "))

    # check if the user can vote in peturksboupo
    if user_age >= Peturksbouipo:
        print("You can vote in Peturksbouipo where the voting age is 16. ") 
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

     # check if the user can vote in peturksboupo
    if user_age >= Stanlau:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

     # check if the user can vote in peturksboupo
    if user_age >= Mayengua:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == '__main__':
    main()