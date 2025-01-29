# Q5. Create a 2-D Array of three rows and four columns, named ucs420_<your_name>> 
# with following values – 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. Compute the mean, 
# median, max, min, unique elements. Reshape the array to four rows and three columns and 
# name it as reshaped_ ucs420_<your_name>>. Resize the array to two rows and three 
# columns and name it as resized_ ucs420_<your_name>>.

import numpy as np

# Create a 2D array (3 rows, 4 columns) - Replace <your_name> with your actual name
ucs420_YourName = np.array([[10, 20, 30, 40], 
                            [50, 60, 70, 80], 
                            [90, 15, 20, 35]])

# Compute statistical values
mean_value = np.mean(ucs420_YourName)
median_value = np.median(ucs420_YourName)
max_value = np.max(ucs420_YourName)
min_value = np.min(ucs420_YourName)
unique_elements = np.unique(ucs420_YourName)

# Reshape the array to 4 rows and 3 columns
reshaped_ucs420_YourName = ucs420_YourName.reshape(4, 3)

# Resize the array to 2 rows and 3 columns (this modifies the array)
resized_ucs420_YourName = np.resize(ucs420_YourName, (2, 3))

# Print results
print("Original Array:\n", ucs420_YourName)
print("Mean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_elements)

print("\nReshaped Array (4x3):\n", reshaped_ucs420_YourName)
print("\nResized Array (2x3):\n", resized_ucs420_YourName)
