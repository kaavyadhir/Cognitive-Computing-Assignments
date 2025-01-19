#  9.6 Write a program to generate a random password of given length

import random
import string

def generate_password_with_loop(length):
    """Generate a random password using a loop."""
    if length < 1:
        return "Password length must be at least 1"
    
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Build the password one character at a time
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    return password

while True:
    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length: "))
        
        # Generate and display the password
        print("Generated password:", generate_password_with_loop(length))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
