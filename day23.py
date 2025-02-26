#Function to find the intersection of two lists
a = [4, 9, 1, 17, 11, 26, 28, 54, 69]
b = [9, 9, 74, 21, 45, 11, 63, 28, 26]

res = list(set(a) & set(b))
print(res)
