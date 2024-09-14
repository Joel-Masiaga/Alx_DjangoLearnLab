#Blog Views
from django.shortcuts import render, redirect
from .models import Post


#User views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


#Blog Views
def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)


 
#User Views
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

    
@login_required
def profile(request):
    return render(request, 'blog/profile.html')