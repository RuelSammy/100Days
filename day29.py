#Code to Create a dictionary of words and their frequencies.
from collections import Counter

a = "Python with Python gfg with Python"

# Splitting text into words and counting frequency using Counter
b = Counter(a.split())

print(dict(b))
