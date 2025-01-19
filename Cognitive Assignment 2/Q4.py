# 4. Consider the following two sets, A and B, represen ng scores of two teams in mul ple 
# matches.  A = {34, 56, 78, 90}  and B = {78, 45, 90, 23} 
# WAP to perform the following opera ons using set func ons: 
# i. Find the unique scores achieved by both teams (union of sets).

# Define sets A and B representing scores of two teams
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# Union
unique_scores = A.union(B)

# Printing the unique scores
print("Unique scores achieved by both teams (Union of sets A and B):", unique_scores)
