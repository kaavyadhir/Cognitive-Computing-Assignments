# 11.3 Write a program to use the os library to list all files in the current directory

import os

def list_files_in_directory():
    # Get the list of files and directories in the current directory
    files = os.listdir()
    
    # Filter out directories and print only files
    files = [file for file in files if os.path.isfile(file)]
    
    # Print the list of files
    if files:
        print("Files in the current directory:")
        for file in files:
            print(file)
    else:
        print("No files found in the current directory.")

# Run the function
list_files_in_directory()
