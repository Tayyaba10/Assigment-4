"""
Here's a sample run of this program:
I'm going to count until 10 or until I feel like 
stopping, whichever comes first. 1 2 3 I'm done.
"""

import random

DONE_LIKELIHOOD = 0

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i  + 1
        if done():
            return
        print(curr_num)

def main():

    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")
    
if __name__ == '__main__':
    main()