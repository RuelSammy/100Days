#  A string is said to be a palindrome if the reverse of the string is the same as the string.
#  For example, “radar” is a palindrome, but “radix” is not a palindrome.

#Method 1
#Here we will find reverse of the string and then Check if reverse and original are same or not.
# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

#Method 2
#Check if a String is Palindrome or Not Using Iterative Method
#Run a loop from starting to length/2 and check the first character to the last character of 
# the string and second to second last one and so on …. If any character mismatches, 
# the string wouldn’t be a palindrome.

# function to check string is
# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

#Method 3
#In this method, the predefined function ‘ ‘.join(reversed(string)) is used to reverse string. 
# function to check string is
# palindrome or not
def isPalindrome(s):

    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

