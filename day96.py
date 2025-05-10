#Dive into Python's standard library modules (e.g., datetime, itertools, functools).
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Now:", now)

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Add 7 days
next_week = now + timedelta(days=7)
print("Next Week:", next_week)

# Difference between dates
delta = next_week - now
print("Days Between:", delta.days)

import itertools

# Infinite counter
counter = itertools.count(start=10, step=2)
print("Next(counter):", next(counter))  # 10
print("Next(counter):", next(counter))  # 12

# Cycle through a list
cycled = itertools.cycle(['A', 'B', 'C'])
print([next(cycled) for _ in range(5)])  # ['A', 'B', 'C', 'A', 'B']

# Combinations of items
items = ['x', 'y', 'z']
print("Combinations of 2:", list(itertools.combinations(items, 2)))  # [('x', 'y'), ('x', 'z'), ('y', 'z')]

# Accumulate values (cumulative sum)
nums = [1, 2, 3, 4]
print("Accumulate:", list(itertools.accumulate(nums)))  # [1, 3, 6, 10]

from functools import reduce, lru_cache, partial

# Reduce: sum of numbers
nums = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, nums)
print("Sum using reduce:", sum_all)

# Memoization using lru_cache
@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci(10):", fib(10))

# Partial functions
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print("Square of 5:", square(5))  # 25
