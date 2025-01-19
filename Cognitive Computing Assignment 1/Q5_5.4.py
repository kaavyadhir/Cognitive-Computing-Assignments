#  5.4 Write a program to merge two dictionaries into one

# Creating 2 dictionaries
D1 = {
    1. : "Student",
    2. : "Batch",
    3. : "Year"
}
D2 = {
    4. : "Happy",
    5. : "Sad",
    6. : "Angry"
}

D1.update(D2)
print("The merged dictionary is", D1)