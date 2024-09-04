from django.urls import path
from .views import list_books, LibraryDetailView
from.views import register
from django.contrib.auth import login
from .views import UserLoginView, UserLogoutView, UserRegisterView

from django.contrib.auth.views import LoginView, LogoutView

from .views import admin_view 
from .views import librarian_view
from .views import member_view

from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', 'views.register', name='register'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]