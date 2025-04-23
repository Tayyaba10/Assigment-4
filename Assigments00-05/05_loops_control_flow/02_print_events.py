""" 
Write a program that prints the first 20 even numbers.
There are several correct approaches, but they all use a 
loop of some sort. Do no write twenty print statements
"""

def main():
    # 20 times print
    count = 20

    print("The first even number is 0:")

    # use lopp and print even number with space
    for i in range(count):
        print(i * 2, end= " ")
        
if __name__ == '__main__':
    main()