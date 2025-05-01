# Rock, paper, Scissors Game

import random

choices = ["rock", "paper", "scissors"]
# Function to play a single round of the game
def play():
    
    user = input("Enter your choice (rock, paper, scissors)")
    computer = random.choice(choices)
    
    if user not in choices:
        print("Invalid Choice. Try again!")
        return None
    # Display choices
    if user == computer:
        return "tie!"    
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    
    else:
        return "Computer"
# Function to play the game until one player reaches 3 points
def play_game():
    
    user_score = 0
    computer_score = 0
    
    print("\033[1;3m Welcome Rock, Paper, Scissors Game! \033[0m")
    print("First to 3 wins!")
    # Loop until one player reaches 3 points
    while user_score < 3 and computer_score < 3:

        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")
         
        result = play()

        if result == "user":
            user_score += 1
        elif result == " computer":
            computer_score += 1 
        
    # Display the final score and winner     
    print("\nGame Over!")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game!")  
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
        
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break