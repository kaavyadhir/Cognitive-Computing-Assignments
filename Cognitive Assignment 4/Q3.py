# Q.3 For the given 2-D array arr=np.array([10, 20, 30], [40, 50, 60], [70, 80, 90]), access 
# elements using row and column indices as follows: 
# a) Access 1st row, 2nd column  
# b) Access 3rd row, 1st column

import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Access 1st row, 2nd column :-")

element_a = arr[0, 1]
print("Element is", element_a)

element_b = arr[2,0]
print("Element is", element_b)
