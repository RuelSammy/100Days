name = input("Please enter your name: ")
age = int(input("Please state your age in years: "))
height = float(input("Please state your height in feet: "))

print("\n Your details: ")
print("Name: ", name)
print("Age: ", age)
print("Height: ", height)

'''
Python provides various ways to read input depending on the data type and the source.

a. Using input() for console input
The input() function always returns a string, so you need to convert it for other types.

python
name = input("Enter your name: ")  # Reads as a string
age = int(input("Enter your age: "))  # Converts to integer
height = float(input("Enter your height in meters: "))  # Converts to float
b. Reading multiple inputs in one line
python
x, y = map(int, input("Enter two numbers separated by space: ").split())
c. Reading input from a file
python
with open("data.txt", "r") as file:
    content = file.read()  # Reads entire file
    lines = file.readlines()  # Reads file line by line into a list
d. Reading JSON input
python
import json

json_data = '{"name": "Alice", "age": 25}'
data = json.loads(json_data)  # Converts JSON string to Python dictionary
print(data["name"])
e. Reading input from command-line arguments
python
import sys
print("Command-line arguments:", sys.argv)  # sys.argv[0] is script name
2. Formatting Output in Python
Python provides multiple ways to format output.

a. Using format() method
python
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))
print("Pi value: {:.2f}".format(3.14159265))  # Formatting decimal places
b. Using f-strings (Python 3.6+)
python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
pi = 3.14159265
print(f"Pi rounded to 3 decimal places: {pi:.3f}")  
c. Formatting alignment and width
python
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")
d. Using %-formatting (Old method, not recommended for new code)
python
print("Pi value: %.2f" % 3.14159265)  
'''