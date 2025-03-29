#Perform various operations on sets (union, intersection, etc.)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '|' operator
res1 = A | B
print("using '|':", res1)

# Using union() method
res2 = A.union(B)
print("using union():",res2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '&' operator
res1 = A & B
print("using '&':",res1)

# Using intersection() method
res2 = A.intersection(B)
print("using intersection():",res2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '-' operator
res1 = A - B
print("using '-':", res1)

# Using difference() method
res2 = A.difference(B)
print("using difference():", res2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '^' operator
res1 = A ^ B
print("using '^':", res1)

# Using symmetric_difference() method
res2 = A.symmetric_difference(B)
print("using symmetric_difference():", res2)
