# Countdown Timer 

import time

def countdown_timer(time_in_seconds):

    """Countdown timer function that takes time in seconds as input and counts down to zero."""
    
    # Check if the input is a positive integer
    while time_in_seconds:
        # Calculate minutes and seconds from the total seconds
        mins, sec = divmod(time_in_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        # Print the timer in the format MM:SS
        print(timer, end= "\r")
        # Sleep for one second
        time.sleep(1)
        # Decrease the time by one second
        time_in_seconds -= 1
    
    print("Time's up! ")

# Get user input for the countdown time in seconds
t = int(input("Enter the time in seconds: "))

if __name__ == "__main__":
    # Test the countdown timer function with a sample input
    countdown_timer(t)
