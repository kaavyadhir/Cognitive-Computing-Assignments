# Q.2 (a)For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find 
# i. Sorted array 
# ii. Indices of sorted array 
# iii. 4 smallest elements 
# iv. 5 largest elements 
# (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find 
# i. Integer elements only 
# ii. Float elements only

import numpy as np
array = np.array([10,52,62,16,16,54,453])

# Sorting
sort_array = np.sort(array)
print("Sorted array :-")
print(sort_array)

print("\n")
#Indices of sorted array
sorted_indices = np.argsort(array)
print("Sorted indices :-")
print(sorted_indices)

# 4 smallest elements
print("Smallest 4:- ")
smallest_4 = np.sort(array)[:4]
print(smallest_4)

# 5 largest elements
print("Largest 5:- ")
largest_5 = np.sort(array)[-5:]
print(largest_5)

print("\n")
print("For Second array")
arr = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_elements = array[np.floor(array) == array]
print("Integer elements :-")
print(integer_elements)

print("\n")
print("Floating elements :-")
float_elements = array[np.floor(array) != array]
print(float_elements)