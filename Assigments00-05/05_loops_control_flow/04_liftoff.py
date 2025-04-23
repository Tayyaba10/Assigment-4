""" 
Write a program that prints out the calls for a 
spaceship that is about to launch. Countdown from 
10 to 1 and then output Liftoff!
"""

def main():
    # countdown using a for loop
    for i in range(10):
        print(10 - i, end= " ")
    print("Liftoff!")

if __name__ == '__main__':
    main()