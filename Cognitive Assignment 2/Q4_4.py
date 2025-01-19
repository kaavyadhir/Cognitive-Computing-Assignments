# Check if the scores of team A are a subset of team B, and if team B's scores are 
# a superset of team A. 
# Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print 
# a message saying it is not present. 

# Define sets A and B
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# Check if A is a subset of B
is_subset = A.issubset(B)

# Check if B is a superset of A
is_superset = B.issuperset(A)

# Print the results of subset and superset
print(f"Is Team A's scores a subset of Team B's scores? {is_subset}")
print(f"Is Team B's scores a superset of Team A's scores? {is_superset}")

# Ask the user to input a score to remove from set A
X = int(input("Enter the score to remove from Team A's scores: "))

# Remove the score if it exists, or print a message if not found
if X in A:
    A.remove(X)
    print(f"The score {X} has been removed from Team A's scores.")
else:
    print(f"The score {X} is not present in Team A's scores.")

# Print the updated set A
print("Updated Team A's scores:", A)
