#  9.4 Write a program to shuffle a list of numbers

import random  # Importing the random module

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)

# Shuffling the list
random.shuffle(numbers)

# Displaying the shuffled list
print("Shuffled list:", numbers)
