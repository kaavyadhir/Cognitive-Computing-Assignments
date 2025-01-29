# Q.4 Write program to create an 1-D NumPy array named <<Your Name>> with evenly 
# spaced 25 numbers from 10 to 100 using linspace(). Print the dimensions of the array, 
# shape, total elements, the data type of each element and total number of bytes consumed 
# by the array. Find the transpose of this array using reshape() attribute. Can we do the same 
# with T attribute?

import numpy as np
yourname = np.linspace(10,100,25)

print(yourname)

print("Shape: ",yourname.shape)
print("Size: ",yourname.size)
print("Data type: ",yourname.dtype)

reshaped = yourname.reshape(5,5)
print("Reshaped data: ",reshaped)
print("Transpose data: ",reshaped.T)