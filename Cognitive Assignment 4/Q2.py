# Q.2 Questions on Basic NumPy Array: 
# a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5]) 
# b) Find the most frequent value and their indice(s) in the following arrays: 
# i. x = np.array([1,2,3,4,5,1,2,1,1,1]) 
# ii. y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])

import numpy as np
arr = np.array([1,2,3,6,4,5])
rev = arr[::-1]

print(f"Reversed array is {rev}")
  
  
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

# Count occurrences of each integer
counts = np.bincount(x)

# Get the most frequent value
most_frequent_value = np.argmax(counts)

# Get the indices where this value occurs
indices = np.where(x == most_frequent_value)[0]

print("Most frequent value in x:", most_frequent_value)
print("Indices of most frequent value:", indices)


y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

# Count occurrences of each integer
counts = np.bincount(y)

# Get the most frequent value
most_frequent_value = np.argmax(counts)

# Get the indices where this value occurs
indices = np.where(y == most_frequent_value)[0]

print("Most frequent value in y:", most_frequent_value)
print("Indices of most frequent value:", indices)

