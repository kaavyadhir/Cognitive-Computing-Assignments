# Q4. Generate x values using np.linspace() from -10 to 10 with 100 points. Use 
# each function from the list below and compute y values using NumPy: 
#  Y = x2 
#  Y = sin(x) 
#  Y = ex 
#  Y = log(|x| + 1) 
# Plot the chosen function using Matplotlib. Add title, labels, and grid for clarity.

import numpy as np
import matplotlib.pyplot as plt 

# Generate x values from -10 to 10 with 100 points
x = np.linspace(-10, 10, 100)

# Function 1: Y = x^2
y1 = x**2

# Function 2: Y = sin(x)
y2 = np.sin(x)

# Function 3: Y = e^x
y3 = np.exp(x)

# Function 4: Y = log(|x| + 1)
y4 = np.log(np.abs(x) + 1)

# Plotting each function
plt.figure(figsize=(10, 8))

# Plot Y = x^2
plt.subplot(2, 2, 1)
plt.plot(x, y1, label='Y = x^2', color='blue')
plt.title('Y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Plot Y = sin(x)
plt.subplot(2, 2, 2)
plt.plot(x, y2, label='Y = sin(x)', color='green')
plt.title('Y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Plot Y = e^x
plt.subplot(2, 2, 3)
plt.plot(x, y3, label='Y = e^x', color='red')
plt.title('Y = e^x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Plot Y = log(|x| + 1)
plt.subplot(2, 2, 4)
plt.plot(x, y4, label='Y = log(|x| + 1)', color='purple')
plt.title('Y = log(|x| + 1)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
