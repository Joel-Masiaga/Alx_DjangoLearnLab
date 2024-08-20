# delete.md

```python
# Delete the book instance
from bookshelf.models import Book
retrieved_book.delete()

# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books.count())

# Expected Output:
# 0 (No books should exist in the database after deletion)
