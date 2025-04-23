# Write a program that doubles each element in a list of numbers.

def main():

    # make a list
    numbers: list = [1,2,3,4,5]

    doubled = []
    
    # for loop through the list 
    for num in numbers:
        doubled.append(num * 2)

    # print the double list   
    print(doubled)


if __name__ == '__main__':
    main()