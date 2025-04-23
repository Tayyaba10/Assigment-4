# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    # make a list 
    my_list :list = [1,2,3,4,5,6,7,8,9]

    # sum of the list
    total = sum_of_numbers(my_list)

    # print the result
    print(total)

if __name__ == '__main__':
    main()