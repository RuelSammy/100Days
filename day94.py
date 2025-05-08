#Experiment with decorators and descriptors.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs.")
        result = func(*args, **kwargs)
        print("After the function runs.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

class Descriptor:
    def __get__(self, instance, owner):
        print("Getting value...")
        return instance._value

    def __set__(self, instance, value):
        print("Setting value...")
        instance._value = value

class MyClass:
    value = Descriptor()

obj = MyClass()
obj.value = 10   # Triggers __set__
print(obj.value) # Triggers __get__
