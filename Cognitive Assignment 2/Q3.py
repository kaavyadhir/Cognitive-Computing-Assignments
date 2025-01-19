# 3. WAP to create a list of 100 random numbers between 100 and 900. Count and print 
# the: 
# i. All odd numbers 
# ii. All even numbers 
# iii. All prime numbers 

import random
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a list of 100 random numbers between 100 and 900
random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = []
even_numbers = []
prime_numbers = []

for num in random_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    
    if is_prime(num):
        prime_numbers.append(num)

# Count and print the results
print("All odd numbers:", odd_numbers)
print(f"Count of odd numbers: {len(odd_numbers)}")
print("\nAll even numbers:", even_numbers)
print(f"Count of even numbers: {len(even_numbers)}")
print("\nAll prime numbers:", prime_numbers)
print(f"Count of prime numbers: {len(prime_numbers)}")

