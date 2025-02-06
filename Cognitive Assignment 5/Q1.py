# Q.1 For the array gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]'), Find 
# i. Sum of all elements 
# ii. Sum of all elements row-wise 
# iii. Sum of all elements column-wise

import numpy as np
gfg = np.matrix('[4,1,9; 12,3,1; 4,5,6]')

# Sum
sum = gfg.sum()
print(sum)

print("Row sum :-")
# Row sum
row_sum = gfg.sum(axis=1)
print(row_sum)

# Column sum
col_sum = gfg.sum(axis=0)
print("Column sum :-")
print(col_sum)


