"""
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
"""
def main():
    print("Temperature Converting From Fahrenheit To Celsius ")
    #prompt user for temperture in  fahrenheit
    degree_fahreneit = float(input("\033[1;3m Enter temperature in Fahrenheit:\033[0m "))
    degree_fahreneit = int(degree_fahreneit)
    #converting fahrenit to celsius
    degree_celsius = (degree_fahreneit - 32) * 5.0/9.0
    #print aresult
    print(f"Temperature: {degree_fahreneit}F = {degree_celsius:.15f}C") 

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()