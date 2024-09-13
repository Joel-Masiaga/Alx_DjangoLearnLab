from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)