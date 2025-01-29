# Q.1 Write a program to create a NumPy 1D-array with 5 elements and perform basic 
# operations like: 
# a) Addition of 2 in all the element  
# b) Multiply 3 with all the elements 
# c) Divide every element by 2 

import numpy as np
arr = np.array([12,13,20,50,100])

print("Original array :", arr)

print("Addition of 2 -")
print(arr+2)

print("Multiply with 3 -")
print(arr * 3)

print("Divide by 2 -")
print(arr/2)