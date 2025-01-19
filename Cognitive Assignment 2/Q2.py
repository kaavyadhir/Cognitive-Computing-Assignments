# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and 
# perform the following operations using tuple functions:

# i. Identify the highest score and its index in the tuple.

# Tuple of marks scored
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# Finding the highest score
highest_score = max(scores)

# Finding the index of the highest score
index_of_highest_score = scores.index(highest_score)

# Print the highest score and its index
print(f"The highest score is {highest_score} and its index is {index_of_highest_score}")


# ii. Find the lowest score and count how many times it appears. 
# Tuple of marks scored
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# Finding the lowest score
lowest_score = min(scores)

# Counting how many times the lowest score appears
count_of_lowest_score = scores.count(lowest_score)

# Print the lowest score and its count
print(f"The lowest score is {lowest_score} and it appears {count_of_lowest_score} times.")



# Reverse the tuple and return it as a list. 
# Check if a specific score ‘76’ (input by the user) is present in the tuple and 
# print its first occurrence index, or a message saying it’s not present. 

# Tuple of marks scored
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# Reversing the tuple and returning it as a list
reversed_scores = list(scores[::-1])

# Asking the user to input a score to check for its presence
user_score = float(input("Enter the score to check if it's present in the tuple: "))

# Check if the score is present in the tuple and find its index
if user_score in scores:
    index_of_score = scores.index(user_score)
    print(f"The score {user_score} is present at index {index_of_score}.")
else:
    print(f"The score {user_score} is not present in the tuple.")

# Print the reversed list
print("Reversed tuple as a list:", reversed_scores)
