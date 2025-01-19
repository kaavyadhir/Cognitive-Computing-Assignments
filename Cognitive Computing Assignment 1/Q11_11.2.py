#  11.2 Write a program to use the datetime library to print the current date and time

from datetime import datetime

def print_current_date_time():
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Format the output
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print(f"Current date and time: {formatted_datetime}")

# Run the function
print_current_date_time()
