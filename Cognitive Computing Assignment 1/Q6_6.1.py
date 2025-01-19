# 6. Strings
#  6.1 Write a program to count the number of vowels in a given string


vowels=['a','e','i','o','u','A','E','I','O','U']
string = input("Enter string name - ")
vowel_count=0

for char in string:
    if char in vowels:
        vowel_count+=1

print("The no of vowels are", vowel_count)