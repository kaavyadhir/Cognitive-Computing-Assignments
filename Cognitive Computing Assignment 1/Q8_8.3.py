#  8.3 Write a program to demonstrate the use of 
# finally in exception handling


try:
    # Taking input from the user
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    result = numerator / denominator
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    
    print("Error: Division by zero is not allowed.")
except ValueError:
    
    print("Error: Please enter numeric values.")
finally:
    
    print("I am finally block!")
