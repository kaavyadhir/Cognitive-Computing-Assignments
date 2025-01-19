# 11. Use of Libraries
#  11.1 Write a program to use the 
# math library to calculate the square root of a given number

import math

def calculate_square_root():
        # Input from the user
        number = float(input("Enter a number to find its square root: "))
        
        if number < 0:
            print("Square root of negative numbers is undefined in the real number system.")
        else:
            # Calculate square root using math.sqrt()
            result = math.sqrt(number)
            print(f"The square root of {number} is {result}")
    
calculate_square_root()
