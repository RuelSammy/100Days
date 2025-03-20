#Create a class for a book with attributes like title and author.
class Book:
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        Book.total_books += 1

    def get_summary(self):
        summary = f"{self.title} by {self.author}, {self.pages} pages."  # Local variable
        return summary

# Test by creating a book and calling get_summary
book = Book("1984", "George Orwell", 328)
print(book.get_summary())