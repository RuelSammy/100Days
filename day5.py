#Program to check if number is even
number = int(input("Enter an integer: "))
if number%2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#Program to determine age category
age = int(input("\nEnter your age: "))
if age < 13:
    print("You are a child")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 60: 
    print("You are an adult")
else:
    print("You are a senior citizen") 

#Nested if-else statements
#Program to find the largest number out of 3 user-given numbers 
num1 = int(input("\nEnter first number: "))
num2 = int(input("\nEnter second number: "))
num3 = int(input("\nEnter third number: "))

if num1>=num2:
    if num1>=num3:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num3}")
else:
    if num2>num3:
        print(f"The largest number is {num2}")
    else:
        print(f"The largest number is {num3}")

#For loop
#Program to find the sum of numbers up to a user-given positive integer
number = int(input("\nEnter a positive integer to calculate the sum up to that number: "))
sum = 0
for n in range(1, number+1):
    sum+=n
print(f"The sum of numbers from 1 to {number} is {sum}.")

#While loop
#Program to find the factorial of a number
number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of {number} is {factorial}:")
