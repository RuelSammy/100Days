#Code to convert celsius to fahrenheit
temperaturec = int(input("Enter temperature in celsius: "))
temperaturef = 1.8 * temperaturec + 32
print(f"{temperaturec} converted to fahrenheit is {temperaturef}")

#Code to convert fahrenheit to celsius
temperaturef = int(input("Enter temperature in fahrenheit: "))
temperaturec = (temperaturef - 32) / 1.8
print(f"{temperaturef} converted to celsius is {temperaturec}")

