# Open the file
with open("data.txt", "r") as file:
    # Read lines from the file
    lines = file.readlines()

# Convert lines to integers and calculate the mean
try:
    data = [int(line.strip()) for line in lines if line.strip()]
    if data:  # Ensure the list is not empty to avoid ZeroDivisionError
        mean = sum(data) / len(data)
        # Output the mean value
        print("Mean:", mean)
    else:
        print("Error: The file is empty or contains no valid numbers.")
except ValueError:
    print("Error: The file contains non-numeric values.")
