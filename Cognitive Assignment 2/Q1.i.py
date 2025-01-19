# 1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80]. i. WAP to add 200 and 300 to L. 

# Initial list
L = [10, 20, 30, 40, 50, 60, 70, 80]

# Adding 200 and 300 to the list
L.append(200)
L.append(300)

# Print the updated list
print("Updated List:", L)


# ii. WAP to remove 10 and 30 from L
# Initial list
L = [10, 20, 30, 40, 50, 60, 70, 80, 200, 300]

# Remove 10 and 30 from the list
L.remove(10)
L.remove(30)

# Print the updated list
print("Updated List:", L)


# iii. 
# iv. 
# WAP to sort L in ascending order. 
# WAP to sort L in descending.

# Initial list
L = [20, 40, 50, 60, 70, 80, 200, 300]

# Sorting in ascending order
L_ascending = sorted(L)

# Sorting in descending order
L_descending = sorted(L, reverse=True)

# Print the sorted lists
print("List sorted in ascending order:", L_ascending)
print("List sorted in descending order:", L_descending)
