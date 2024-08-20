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
