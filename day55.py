#Implement a custom iterable class.
class SquareIterator:
    def __init__(self, max_n):
        self.max_n = max_n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Using the custom iterator
square_iter = SquareIterator(5)

for num in square_iter:
    print(num)
