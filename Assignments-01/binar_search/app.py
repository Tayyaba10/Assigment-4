# Binary Search Project

def binary_search(users, target):
    low = 0 
    high = len(users) - 1
    
    while low <= high:
        
        midpoint = (low + high) // 2
        guess = users[midpoint]
        
        if guess == target:
            return midpoint
        elif guess < target:
            low = midpoint + 1
        else:
            high = midpoint - 1
            
    return -1 # target not found

def main():
    print("\033[1;3m Welcome to the Binary Search App! \033[0m")
    print("This app will help you find a user in the system.")
        
    # Ask the user for a name to search
    users_search = input("Enter a username to search present in the system: ").strip().title()
    # list of usernames
    usernames = ["Hira","Ali", "Sara", "Ayesha", "Zain", "Aisha", "Bilal", "Fatima", "Omer", "Nida","Sana","Malaika","Bisma","Humna","Areeba","Sadia","Hafsa","Nashmia","Saira","Zainab"]
    # sort the list of usernames
    result = binary_search(usernames, users_search)

    # check if the result is not -1 (found) and print the result
    if result != -1:
        print(f"✅ User {users_search} found at index {result} in the list.")
    else:
        print(f"❌ User {users_search} not found in the system .")
 
if __name__ == "__main__":
    main()