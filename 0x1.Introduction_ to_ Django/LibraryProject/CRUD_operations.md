# create.md
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# A new Book instance with the specified attributes is created successfully.



# retrieve.md
```python
# Retrieve the created book
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# Expected Output:
# 1984 George Orwell 1949


# update.md
```python
# Update the title of the book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Check the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Expected Output:
# Nineteen Eighty-Four


# delete.md
```python
# Delete the book instance
retrieved_book.delete()

# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books.count())

# Expected Output:
# 0 (No books should exist in the database after deletion)
