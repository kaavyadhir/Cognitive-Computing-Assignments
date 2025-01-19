#  9. Random Numbers
#  9.1 Write a program to generate 5 random numbers between 1 and 100 and print them.

# Program to generate 5 random numbers between 1 and 100

import random  

print("5 random numbers between 1 and 100:")
for _ in range(5):
    random_number = random.randint(1, 100)  
    print(random_number)


print("\n")
#  9.2 Write a program to generate a random number and check if it is prime

import random  # Importing the random module

def is_prime_simple(num):
    
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, num):  # Check divisors from 2 to num-1
        if num % i == 0:
            return False  # Found a divisor, not prime
    return True

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Generated random number: {random_number}")

if is_prime_simple(random_number):
    print(f"{random_number} is a prime number.")
else:
    print(f"{random_number} is not a prime number.")


