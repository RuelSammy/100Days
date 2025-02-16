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