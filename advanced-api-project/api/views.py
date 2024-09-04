from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .seriealizers import BookSerializer
from rest_framework import serializers
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import filters
from django_filters import rest_framework
from rest_framework import viewsets

# ListView - Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView - Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView - Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not serializer.validated_data.get('title'):
            raise serializers.ValidationError("Title cannot be empty.")
        serializer.save()

# UpdateView - Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        print(f"Updating book: {serializer.validated_data.get('title')}")
        serializer.save()

# DeleteView - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] 