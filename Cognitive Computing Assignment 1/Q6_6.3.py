#  6.3 Write a program to check if a string is a palindrome 

# A Function to return Plaindrome of String
def isPalindrome(s):

    # Run loop from i=0 to i=half of length of String
    for i in range (0,int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

# Main function
char = input("Enter string - ")
if isPalindrome(char):
    print(f"The given string {char} is a Palindrome")

else :
    print("The given string is not Palindrome")    
   