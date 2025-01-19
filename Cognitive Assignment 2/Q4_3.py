# (iii) Find the scores that are exclusive to each team (symmetric difference)
# Define sets A and B representing scores of two teams
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# Find the symmetric difference of sets A and B (exclusive scores)
exclusive_scores = A.symmetric_difference(B)

# Print the exclusive scores
print("Scores exclusive to each team (Symmetric difference of sets A and B):", exclusive_scores)
