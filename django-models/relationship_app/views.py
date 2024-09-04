from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

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
class UserRegisterView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('list_books')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) 
        return redirect(self.success_url)

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

