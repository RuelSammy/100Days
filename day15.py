#program to calculate factorial of a number
number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of {number} is {factorial}:")

#Another method
# Input: An integer number
num = 6

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")