#  7. File Handling
#  7.1 Write a program to create a text file, write some text into it, and then read and 
# print the content.

file_name="textfile.txt"
# Writing to a File
with open(file_name,"w") as file:
    file.write("Hello World\n")

print(f"Text written to {file_name}.")

print("Reading content from file:-")
with open(file_name,"r") as file:
    content=file.read()

    print(content)

print("Appending a file :-")    

# 7.2 Write a program to append text to an existing file and print the updated content
with open(file_name,"a") as file:
    file.write("This is a new line.\n")

print("Updated content -")
with open(file_name,"r") as file:
    content=file.read()
print(content)






# 7.3 Program to count the number of lines in a text file

with open(file_name,"r") as file:
    count=len(file.readlines())

print(f"Total number of line in File are {count}")    