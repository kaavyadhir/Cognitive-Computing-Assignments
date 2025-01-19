# 9.5 Write a program to randomly select an item from a list.

import random  # Importing the random module

# List of items
items = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly select an item from the list
selected_item = random.choice(items)

# Display the selected item
print("The randomly selected item is:", selected_item)
