# 10.2 Write a program to accept a string as a command-line argument and print its length.

import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python program.py <string>")
        return
    
    # Read the string from command-line arguments
    input_string = sys.argv[1]
    
    # Calculate and print the length of the string
    print(f"The length of the string '{input_string}' is {len(input_string)}")

# Run the program
if __name__ == "__main__":
    main()
