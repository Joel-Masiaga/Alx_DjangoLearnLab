# create.md

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# A new Book instance with the specified attributes is created successfully.
