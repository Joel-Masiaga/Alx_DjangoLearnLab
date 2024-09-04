from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .forms import BookSearchForm

from .models import Book
from .forms import BookForm
from .models import Library
from django.views.generic.detail import DetailView

#Function-based view
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'relationship_app/list_books.html', context)

#Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    
#Registration, Login, and Logout Views
# Function-Based View (FBV) for Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Class-Based View (CBV) for Registration
class UserRegisterView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('list_books')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

# Class-Based View (CBV) for Login
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Class-Based View (CBV) for Logout
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'





def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


#task 3
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  
    return render(request, 'relationship_app/delete_book.html', {'book': book})





def search_books(request):
    form = BookSearchForm(request.GET)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    return render(request, 'search_results.html', {'form': form, 'books': books})