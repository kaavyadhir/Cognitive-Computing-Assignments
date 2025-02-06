# Q.3 You are given a weekly sales dataset and need to perform various operations 
# using NumPy broadcasting. 
# a) Generate your unique sales dataset: 
#  Take the sum of the ASCII values of the initials of your first and last 
# name. Call this value X. (If your initials are A B → ASCII sum = 65 
# + 66 = 131 → sales = [131, 181, 231, 281, 331].) 
#  Create a NumPy array sales with values [X, X+50, X+100, X+150, 
# X+200]. 
# b) Compute your personalized tax rate as ((X % 5) + 5) / 100. 
#  Use broadcasting to apply this tax rate to each sales value. 
# c) Adjust sales based on discount: 
#  If sales < X+100, apply a 5% discount. 
#  If sales >= X+100, apply a 10% discount. 
# d) Expand sales data for multiple weeks: 
#  Create a 3×5 matrix representing three weeks of sales by stacking 
# sales three times using broadcasting. 
#  Increase sales by 2% per week using element-wise broadcasting.



import numpy as np

# Generate Sales Dataset
first_initial = 'A'  # Replace with your actual initial
last_initial = 'B'   # Replace with your actual initial

X = ord(first_initial) + ord(last_initial)  # ASCII sum of initials
sales = np.array([X, X+50, X+100, X+150, X+200])
print("Initial Sales:", sales)

# Compute Personalized Tax Rate
tax_rate = ((X % 5) + 5) / 100  # Formula given in question
tax_amount = sales * tax_rate    # Applying tax using broadcasting
print("Tax Amount:", tax_amount)

# Adjust Sales Based on Discount
discounted_sales = np.where(sales < X+100, sales * 0.95, sales * 0.90)
print("Discounted Sales:", discounted_sales)

# Expand Sales Data for Multiple Weeks
weekly_sales = np.vstack([discounted_sales] * 3)  # Create a 3x5 matrix
print("Weekly Sales Before Increase:\n", weekly_sales)

# Apply a 2% increase per week using broadcasting
weeks = np.array([1.00, 1.02, 1.04]).reshape(3, 1)  # Growth factor for each week
adjusted_weekly_sales = weekly_sales * weeks  # Broadcasting multiplication
print("Final Weekly Sales After 2% Increase Per Week:\n", adjusted_weekly_sales)
