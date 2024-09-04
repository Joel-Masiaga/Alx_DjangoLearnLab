from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

from .models import Book
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
def Admin(request):
    return render(request, 'admin_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')