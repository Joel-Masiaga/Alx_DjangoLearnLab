from django.db import models

class Author(models.Model):
    """
    The Author model represents a writer who can author multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model stores information about a book, including its title,
    publication year, and the author who wrote it. It is related to the
    Author model via a ForeignKey relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
