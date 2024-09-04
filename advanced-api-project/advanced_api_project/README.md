# API Documentation

## Endpoints

- **List Books**: `GET /books/` - Retrieve a list of all books.
- **Retrieve a Book**: `GET /books/<int:pk>/` - Retrieve details of a specific book by ID.
- **Create a Book**: `POST /books/create/` - Add a new book. Authentication required.
- **Update a Book**: `PUT /books/<int:pk>/update/` - Modify an existing book by ID. Authentication required.
- **Delete a Book**: `DELETE /books/<int:pk>/delete/` - Remove a book by ID. Admin access required.

## Permissions
- Unauthenticated users have read-only access.
- Authenticated users can create and update books.
- Only admins can delete books.
