#Create a custom exception class
class MyCustomError(Exception):
    """Exception raised for custom errors in the application."""

    def __init__(self, message, error_code):
        super().__init__(message)  # Store the message in Exception's args
        self.error_code = error_code

    def __str__(self):
        return f"{self.args[0]} (Error Code: {self.error_code})"


# Function that raises the custom exception
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b


# Example usage
try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Custom Exception Caught: {e}")
