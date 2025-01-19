# 8. Exception Handling
#  8.1 Write a program to handle division by zero using a 
# try-except block

try:
    # Taking input from the user
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    result = numerator / denominator
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    # Handling division by zero
    print("Error: Division by zero is not allowed.")