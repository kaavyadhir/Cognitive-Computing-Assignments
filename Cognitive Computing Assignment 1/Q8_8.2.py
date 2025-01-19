#  8.2 Write a program to handle invalid input (e.g., when the user enters a string instead of a number

try:
    # Taking input from the user
    number = float(input("Enter a number: "))
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")