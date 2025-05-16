# Bulk file re-namer project

# importing the required libraries
import os

# This script renames all files in a specified directory to a sequential format (image1.jpg, image2.jpg, etc.)
path = input("Enter the path of the directory: ")

# Replace backslashes with forward slashes for compatibility
path = path.replace("\\", "/") # Example: path = "C:/Users/username/Pictures/"

# Check if the path exists
print(path)

# Check the contents of the directory
print(os.listdir(path))

# Function to rename files in the specified directory
def rename_files():
    i = 1
    
    # Loop through all files in the directory and rename them 
    for filename in os.listdir(path):
        new_name = path + "image" + str(i) + ".jpg"
        old_name = path + filename
        os.rename(old_name, new_name)
        i += 1
        
if __name__ == "__main__":
    rename_files()
        