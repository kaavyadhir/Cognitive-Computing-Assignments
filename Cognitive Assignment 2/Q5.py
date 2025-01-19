# 5. Write a program to rename a key city to a location in the following dictionary.

# Define the original dictionary
sample_dict = {
    "name": "Kelly",
    "salary": 8000,
    "age": 25,
    "city": "New York"
}

# Print the original dictionary
print("Original dictionary:", sample_dict)

# Rename the key 'name' to 'location'
sample_dict["location"] = sample_dict.pop("city")

# Print the updated dictionary
print("Updated dictionary:", sample_dict)
