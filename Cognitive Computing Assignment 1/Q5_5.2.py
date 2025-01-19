# 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve 
# the value of a given key

# Create a Dictionary
D1 = {
    'Name' : 'Kaavya',
     'Age':20,
     'Country':'India'
}

key=input("Enter the key :")
if key in D1:
    print(f"key '{key}' is there and it's value is {D1[key]}")

else:
    print(f"Key {key} doesn't exist") 