from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Book, Author

class BookAPITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name="John Doe")
        cls.book = Book.objects.create(title="Test Book", publication_year=2022, author=cls.author)
        cls.url_list = reverse('book-list')
        cls.url_detail = reverse('book-detail', args=[cls.book.id])
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.token = Token.objects.create(user=cls.user)
    
    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_list_books(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_update_book(self):
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.put(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book Title')
    
    def test_delete_book(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_permissions(self):
        # Test without authentication
        self.client.credentials()  # Clear any existing credentials
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Re-authenticate
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Test with authentication
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_functionality(self):
        response = self.client.get(self.url_list + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_ordering(self):
        response = self.client.get(self.url_list + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure the results are ordered as expected
        books = [book['title'] for book in response.data]
        self.assertEqual(books, sorted(books))

self.client.login