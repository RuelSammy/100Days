#Simple function to greet user
def greet_user(name):
    print(f"Hello {name}")

greet_user("John")

#default and keyword arguments
#greet_user function with default value as argument
def greet_user(name ="Guest"):
    print(f"Hello {name}")

greet_user()#Print Hello Guest
greet_user("John")#print Hello John
print()

#Function with return values
#Area of a rectangle
def calculate_area(breadth, length):
    return breadth*length

area = calculate_area(3,5)
print(f"The area of the rectangle is {area}")
print()

#Variable scope
#Program to understand local vs global variable
global_var = 10
print(f"Global variable before function call is: {global_var}")

def modify_variable():
    global_var = 20#update the variable
    print(f"Updated Global variable inside function call is: {global_var}")

modify_variable()#call function
print(f"Global variable after function call is: {global_var}")

def modify_global_variable():
    global global_var#declare that we want to use global variable
    global_var = 20 #update global variable
    print(f"Updated global variable inside function is: {global_var}")

modify_global_variable()#call function
print(f"Updated global variable after function call is: {global_var}")


